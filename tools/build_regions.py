#!/usr/bin/env python3
"""Publishes region flags and names from the regions/ folders.

Run from the repo root (GitHub runs it for you on every push that touches regions/):
  python3 tools/build_regions.py

Reads
  regions/XX/regions.json     your choices, one entry per region (see regions/README.md)
  regions/XX/<image>          flags you uploaded (PNG, JPG or SVG)
  build/base-names.json       the names built into the app (from the app repo)
  build/auto-flags/XX.flagpack, build/auto-credits.json
                              the automatic flags from Wikidata (from the app repo)
Writes
  flags/XX.flagpack, flags/credits.json, FLAGS.md   what the app downloads
  names.json                  names that differ from the app's built-in ones
  manifest.json               "flags" and "names" entries, versions bumped on change
  regions/XX/README.md, regions/README.md           status pages and to-do lists

Exits with status 2 (after writing everything it could) if any entry had a problem.
"""
import glob, hashlib, html, io, json, os, re, shutil, struct, subprocess, sys, time, urllib.parse

WIDTH = 240
UA = "WayfarerRegionBuilder/1.0 (data build script)"
IMAGE_TYPES = (".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif")
problems = []


def problem(cc, text):
    problems.append((cc, text))
    print(f"::warning title=regions/{cc}::{text}" if os.environ.get("GITHUB_ACTIONS") else f"  {cc}: {text}")


def write_if_changed(path, data):
    data = data.encode() if isinstance(data, str) else data
    if os.path.exists(path) and open(path, "rb").read() == data:
        return
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "wb").write(data)


def dumps(obj):
    return json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=True) + "\n"


def entries_json(entries):
    """One region per line, so the file is easy to edit by hand."""
    lines = [f"  {json.dumps(code)}: {json.dumps(e, ensure_ascii=False)}" for code, e in entries.items()]
    return "{\n" + ",\n".join(lines) + "\n}\n"


# MARK: Flag packs ("WFFL": magic, UInt32 version, UInt64 index length, JSON index, PNGs)

def read_pack(path):
    if not os.path.exists(path):
        return {}
    d = open(path, "rb").read()
    n = struct.unpack("<Q", d[8:16])[0]
    index = json.loads(d[16:16 + n])["f"]
    body = d[16 + n:]
    return {code: body[o:o + l] for code, (o, l) in index.items()}


def make_pack(images):
    index, blob = {}, b""
    for code in sorted(images):
        index[code] = [len(blob), len(images[code])]
        blob += images[code]
    head = json.dumps({"f": index}, separators=(",", ":")).encode()
    return b"WFFL" + struct.pack("<IQ", 1, len(head)) + head + blob


# MARK: Images

def to_png(src_bytes, ext):
    """A PNG about WIDTH px wide, from an uploaded image."""
    if ext == ".svg":
        if not shutil.which("rsvg-convert"):
            raise RuntimeError("SVG needs rsvg-convert (installed on GitHub; locally: brew install librsvg)")
        return subprocess.run(["rsvg-convert", "-w", str(WIDTH), "-f", "png"], input=src_bytes,
                              check=True, capture_output=True).stdout
    try:
        from PIL import Image
    except ImportError:
        Image = None
    if Image:
        im = Image.open(io.BytesIO(src_bytes))
        im = im.convert("RGBA")
        if im.width > WIDTH:
            im = im.resize((WIDTH, max(1, round(im.height * WIDTH / im.width))), Image.LANCZOS)
        out = io.BytesIO()
        im.save(out, "PNG", optimize=True)
        return out.getvalue()
    if shutil.which("sips"):                       # macOS fallback when Pillow isn't installed
        src, out = "build/.tmp-in" + ext, "build/.tmp-out.png"
        open(src, "wb").write(src_bytes)
        try:
            subprocess.run(["sips", "-s", "format", "png", "--resampleWidth", str(WIDTH), src, "--out", out],
                           check=True, capture_output=True)
            return open(out, "rb").read()
        finally:
            for f in (src, out):
                if os.path.exists(f):
                    os.remove(f)
    raise RuntimeError("needs Pillow (pip install pillow)")


def uploaded_png(path):
    """Converted once per distinct upload, then reused (so packs only change when the image does)."""
    src = open(path, "rb").read()
    key = hashlib.sha256(src).hexdigest()[:24]
    cached = f"build/upload-cache/{key}.png"
    if not os.path.exists(cached):
        write_if_changed(cached, to_png(src, os.path.splitext(path)[1].lower()))
    return open(cached, "rb").read()


def get(url, data=None):
    cmd = ["curl", "-sSfL", "--retry", "2", "--retry-all-errors", "--retry-delay", "2", "--max-time", "60", "-A", UA, url]
    if data is not None:
        cmd += ["--data", data]
    return subprocess.run(cmd, check=True, capture_output=True).stdout


def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def commons(files):
    """{file: {"png": bytes, "page", "license", "author"}} for Wikimedia Commons files (cached)."""
    info_path = "build/commons-cache/info.json"
    info = json.load(open(info_path)) if os.path.exists(info_path) else {}
    todo = sorted(f for f in files if f not in info)
    for i in range(0, len(todo), 40):
        batch = todo[i:i + 40]
        body = urllib.parse.urlencode({"action": "query", "format": "json", "prop": "imageinfo",
                                       "iiprop": "url|extmetadata", "iiurlwidth": WIDTH,
                                       "titles": "|".join("File:" + f for f in batch)})
        try:
            data = json.loads(get("https://commons.wikimedia.org/w/api.php", body))
        except subprocess.CalledProcessError:
            continue
        norm = {n["to"]: n["from"] for n in data["query"].get("normalized", [])}
        for page in data["query"]["pages"].values():
            title = norm.get(page["title"], page["title"])[5:]
            if "imageinfo" not in page:
                info[title] = None
                continue
            ii = page["imageinfo"][0]
            meta = ii.get("extmetadata", {})
            info[title] = {"thumb": ii.get("thumburl") or ii["url"], "page": ii.get("descriptionurl", ""),
                           "license": strip(meta.get("LicenseShortName", {}).get("value")) or "unknown",
                           "author": strip(meta.get("Artist", {}).get("value"))[:200]}
        time.sleep(0.3)
    write_if_changed(info_path, dumps(info))
    out = {}
    for f in files:
        meta = info.get(f)
        if not meta:
            continue
        cached = f"build/commons-cache/{hashlib.sha1(f.encode()).hexdigest()[:20]}.png"
        if not os.path.exists(cached):
            try:
                png = get(meta["thumb"])
            except subprocess.CalledProcessError:
                continue
            if not png.startswith(b"\x89PNG"):
                png = to_png(png, ".jpg")
            write_if_changed(cached, png)
            time.sleep(0.3)
        out[f] = dict(meta, png=open(cached, "rb").read())
    return out


# MARK: Build

def commons_thumb(file, width=48):
    return "https://commons.wikimedia.org/wiki/Special:FilePath/" + urllib.parse.quote(file.replace(" ", "_")) + f"?width={width}"


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")
    base = json.load(open("build/base-names.json"))
    auto_credits = json.load(open("build/auto-credits.json"))

    # 1. Make sure every region has an entry (new regions are added; your edits are kept).
    choices = {}
    for cc, names in sorted(base.items()):
        path = f"regions/{cc}/regions.json"
        if os.path.exists(path):
            try:
                entries = json.load(open(path))
                if not isinstance(entries, dict):
                    raise ValueError("should be { \"CODE\": { … }, … }")
            except ValueError as e:
                problem(cc, f"regions.json can't be read ({e}); this country was skipped and keeps its last published flags and names.")
                choices[cc] = None
                continue
        else:
            entries = {}
        added = False
        for code, name in sorted(names.items(), key=lambda kv: kv[1].casefold()):
            if code not in entries:
                entries[code] = {"name": name.strip()}
                added = True
        if added or not os.path.exists(path):
            write_if_changed(path, entries_json(entries))
        for code, e in entries.items():
            if code not in names:
                problem(cc, f"{code} isn't a region the app knows (typo in the code?); it was ignored.")
            elif not isinstance(e, dict):
                problem(cc, f"{code} should be {{ \"name\": … }}; it was ignored.")
        choices[cc] = {c: e for c, e in entries.items() if c in names and isinstance(e, dict)}

    # 2. Look up every Commons file that's been picked.
    wanted = set()
    for cc, entries in choices.items():
        for code, e in (entries or {}).items():
            flag = e.get("flag")
            if isinstance(flag, str) and flag.lower().startswith("commons:"):
                wanted.add(flag.split(":", 1)[1].strip().removeprefix("File:").replace("_", " "))
    picked = commons(wanted) if wanted else {}

    # 3. Flags and names per country.
    manifest = json.load(open("manifest.json"))
    manifest.setdefault("flags", {})
    published = json.load(open("names.json")) if os.path.exists("names.json") else {}
    old_credits = json.load(open("flags/credits.json")) if os.path.exists("flags/credits.json") else {}
    names_out, credits, status = {}, {}, {}

    for cc, entries in choices.items():
        if entries is None:                    # unreadable file: keep what's published
            names_out.update({c: n for c, n in published.items() if c.startswith(cc + "-")})
            credits.update({c: v for c, v in old_credits.items() if c.startswith(cc + "-")})
            continue
        auto = read_pack(f"build/auto-flags/{cc}.flagpack")
        images, rows = {}, []
        for code, e in entries.items():
            name = e.get("name") if isinstance(e.get("name"), str) and e.get("name").strip() else base[cc][code]
            name = name.strip()
            if name != base[cc][code]:
                names_out[code] = name
            flag, source, preview, note = e.get("flag"), "missing", "", ""
            given = e.get("credit") if isinstance(e.get("credit"), dict) else {}
            if flag is None or flag == "":
                if code in auto:
                    images[code] = auto[code]
                    c = auto_credits.get(code, {})
                    credits[code] = dict(c, name=name)
                    source, preview = "automatic", commons_thumb(c["file"]) if c.get("file") else ""
            elif not isinstance(flag, str):
                problem(cc, f"{code}: \"flag\" should be text.")
            elif flag.lower() == "none":
                source = "none"
            elif flag.lower().startswith("commons:"):
                file = flag.split(":", 1)[1].strip().removeprefix("File:").replace("_", " ")
                meta = picked.get(file)
                if not meta:
                    problem(cc, f"{code}: couldn't find \"{file}\" on Wikimedia Commons (check the exact file name).")
                    if code in auto:
                        images[code] = auto[code]
                        c = auto_credits.get(code, {})
                        credits[code] = dict(c, name=name)
                        source, note = "automatic", "your Commons pick wasn't found"
                        preview = commons_thumb(c["file"]) if c.get("file") else ""
                else:
                    images[code] = meta["png"]
                    credits[code] = {"name": name, "file": file, "source": meta["page"],
                                     "license": given.get("license") or meta["license"],
                                     "author": given.get("author") or meta["author"]}
                    source, preview = "commons", commons_thumb(file)
            else:
                path = f"regions/{cc}/{flag}"
                if os.path.dirname(os.path.normpath(flag)) or not os.path.isfile(path):
                    problem(cc, f"{code}: no file named \"{flag}\" in regions/{cc}/.")
                elif os.path.splitext(flag)[1].lower() not in IMAGE_TYPES:
                    problem(cc, f"{code}: \"{flag}\" isn't an image type the build understands (PNG, JPG or SVG).")
                else:
                    try:
                        images[code] = uploaded_png(path)
                        credits[code] = {"name": name, "file": flag,
                                         "source": given.get("source") or f"regions/{cc}/{flag}",
                                         "license": given.get("license") or "not given",
                                         "author": given.get("author") or "not given"}
                        source, preview = "yours", urllib.parse.quote(flag)
                        if not given.get("license"):
                            note = "add a \"credit\" with the license"
                    except (RuntimeError, subprocess.CalledProcessError, OSError) as err:
                        problem(cc, f"{code}: couldn't convert \"{flag}\" ({err}).")
            rows.append({"code": code, "name": name, "base": base[cc][code], "source": source,
                         "preview": preview, "note": note})

        pack_path = f"flags/{cc}.flagpack"
        if images:
            data = make_pack(images)
            write_if_changed(pack_path, data)
            old = manifest["flags"].get(cc, {})
            sha = hashlib.sha256(data).hexdigest()
            manifest["flags"][cc] = {"file": pack_path, "bytes": len(data), "sha256": sha, "count": len(images),
                                     "v": old.get("v", 0) + (0 if old.get("sha256") == sha else 1)}
        else:
            if os.path.exists(pack_path):
                os.remove(pack_path)
            manifest["flags"].pop(cc, None)
        status[cc] = rows

    # 4. Names, manifest, credits.
    names_data = dumps(names_out).encode()
    write_if_changed("names.json", names_data)
    sha = hashlib.sha256(names_data).hexdigest()
    old = manifest.get("names", {})
    manifest["names"] = {"file": "names.json", "bytes": len(names_data), "sha256": sha, "count": len(names_out),
                         "v": old.get("v", 0) + (0 if old.get("sha256") == sha else 1)}
    write_if_changed("manifest.json", json.dumps(manifest, indent=1, sort_keys=True))
    write_if_changed("flags/credits.json", dumps(credits))

    lines = ["# Region flag credits", "",
             "Most flags come from Wikimedia Commons, via Wikidata's \"flag image\" (P41) for each ISO 3166-2 region;",
             "others were picked by hand in [regions/](regions/). Each image keeps its own license, listed below.",
             "The PNGs are scaled-down copies of the originals.", "",
             "| Region | Code | License | Author | Source |", "|---|---|---|---|---|"]
    for code, c in sorted(credits.items()):
        author = (c.get("author") or "–").replace("|", "/").replace("\n", " ")
        src = c.get("source", "")
        link = f"[{c.get('file', '')}]({src.replace(' ', '%20')})" if src else c.get("file", "")
        lines.append(f"| {c.get('name', '')} | {code} | {c.get('license', '')} | {author} | {link} |")
    write_if_changed("FLAGS.md", "\n".join(lines) + "\n")

    # 5. Status pages.
    country_names = load_country_names()
    by_cc = {}
    for cc, text in problems:
        by_cc.setdefault(cc, []).append(text)
    index = []
    for cc, rows in sorted(status.items()):
        write_if_changed(f"regions/{cc}/README.md", country_page(cc, country_names.get(cc, cc), rows, by_cc.get(cc, [])))
        index.append((cc, country_names.get(cc, cc), rows))
    write_if_changed("regions/README.md", index_page(index))

    print(f"{sum(len(r) for r in status.values())} regions in {len(status)} countries; "
          f"{len(credits)} flags; {len(names_out)} renamed")
    if problems:
        print(f"{len(problems)} problem(s), listed above and on each country's page")
        sys.exit(2)


def load_country_names():
    path = "build/country-names.json"
    return json.load(open(path)) if os.path.exists(path) else {}


def odd_name(n):
    return "/" in n or "(" in n or n.isupper() and len(n) > 4


def country_page(cc, country, rows, issues):
    have = sum(r["source"] not in ("missing", "none") for r in rows)
    missing = [r for r in rows if r["source"] == "missing"]
    odd = [r for r in rows if odd_name(r["name"])]
    out = [f"# {country} ({cc})", "",
           f"{len(rows)} regions · {have} with flags · {len(missing)} missing · "
           f"{sum(r['name'] != r['base'] for r in rows)} renamed", "",
           "Edit [`regions.json`](regions.json) to change names and flags; how-to in [regions/README.md](../README.md).",
           "This page is rebuilt automatically, so don't edit it.", ""]
    if issues:
        out += ["## ⚠️ Problems with your last change", ""] + [f"- {t}" for t in issues] + [""]
    if missing or odd:
        out += ["## To do", ""]
        out += [f"- [ ] **{r['name']}** (`{r['code']}`) has no flag" for r in missing]
        out += [f"- [ ] **{r['name']}** (`{r['code']}`): check the name" for r in odd]
        out.append("")
    labels = {"automatic": "Automatic (Wikidata)", "commons": "Your pick (Commons)", "yours": "Your upload",
              "none": "Hidden", "missing": "—"}
    out += ["## All regions", "", "| Flag | Code | Name | Flag source |", "|---|---|---|---|"]
    for r in rows:
        img = f'<img src="{r["preview"]}" height="20">' if r["preview"] else ""
        name = r["name"] if r["name"] == r["base"] else f"{r['name']} <sub>was {r['base']}</sub>"
        note = f" · {r['note']}" if r["note"] else ""
        out.append(f"| {img} | `{r['code']}` | {name} | {labels[r['source']]}{note} |")
    return "\n".join(out) + "\n"


def index_page(index):
    total = sum(len(r) for _, _, r in index)
    flags = sum(sum(x["source"] not in ("missing", "none") for x in r) for _, _, r in index)
    out = [open("tools/regions-guide.md").read().rstrip(), "",
           "## Countries", "", f"{total} regions in {len(index)} countries, {flags} with flags.", "",
           "| Country | Regions | Flags | Missing | Renamed |", "|---|---|---|---|---|"]
    for cc, name, rows in index:
        have = sum(x["source"] not in ("missing", "none") for x in rows)
        miss = sum(x["source"] == "missing" for x in rows)
        ren = sum(x["name"] != x["base"] for x in rows)
        out.append(f"| [{name}]({cc}/) | {len(rows)} | {have} | {miss or ''} | {ren or ''} |")
    return "\n".join(out) + "\n"


main()
