# Region names and flags

Each country has a folder here with a `regions.json` listing every state, province or region the app knows.
Change a name or pick a flag there, commit, and GitHub rebuilds everything in a minute or two
(watch the **Actions** tab). The app picks up the change the next time it's opened. No app update needed.

Each country folder's page shows every region with its current flag, plus a **To do** list of
regions with no flag and names worth a second look.

## Change a name

```json
"ES-CT": { "name": "Cataluña" }
```

Places you've already marked get the new name too.

## Pick a flag

Three ways, using `"flag"`:

| You write | What it does |
|---|---|
| `"flag": "commons:Flag of Brittany.svg"` | Uses that file from [Wikimedia Commons](https://commons.wikimedia.org) (exact file name, without `File:`). Its license and author are filled in for you. |
| `"flag": "FR-BRE.png"` | Uses an image you uploaded to the same folder (PNG, JPG or SVG; any size, it's scaled down). |
| `"flag": "none"` | Shows no flag for that region. |

Leave `"flag"` out to keep the automatic one (from Wikidata).

For your own uploads, add where it came from, so the credits page stays right:

```json
"FR-BRE": {
  "name": "Bretagne",
  "flag": "FR-BRE.svg",
  "credit": { "author": "…", "license": "Public domain", "source": "https://…" }
}
```

## Editing on github.com

1. Open the country's folder, then `regions.json`, then the pencil icon.
2. Make the change and press **Commit changes**.
3. To add an image: in the country's folder, **Add file → Upload files**.

If something's wrong (a typo in a code, a file that isn't there), the build still publishes everything
else, the Actions run turns red, and the country's page lists the problem at the top.
Watch the commas: every entry but the last ends with one.
