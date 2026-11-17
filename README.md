# Wayfarer Journal: map data

Data the Wayfarer Journal iOS app downloads per country, the first time it's needed:

- **District boundaries** (`admin2-XX.geopack`): simplified county-level (admin-2) boundaries, downloaded when someone opens that country's Districts layer.
- **Cities** (`cities/XX.json`): major cities of 100,000+ people, biggest first, each tagged with the app's region code. Downloaded when someone opens that country's page. From [GeoNames](https://www.geonames.org) (CC BY 4.0).
- **Region flags** (`flags/XX.flagpack`): flags for states and provinces, downloaded when that country's regions are shown. `flags/credits.json` and [FLAGS.md](FLAGS.md) list each flag's author and license.

- `manifest.json` lists every file with its size, SHA-256 checksum and data version (`v`); district files also list their source license.
- `admin2-XX.geopack` files are a binary format: a JSON metadata header followed by MKMapPoint coordinate pairs. They are built by `tools/geobuild.swift` in the app's repository.

District files are derived from [geoBoundaries](https://www.geoboundaries.org) (Runfola et al., 2020, *geoBoundaries: A global database of political administrative boundaries*, PLoS ONE 15(4): e0231866).

See [LICENSE.md](LICENSE.md) for the license of each country's boundaries and [FLAGS.md](FLAGS.md) for the flags.

Rebuild cities with `python3 -I tools/build_city_packs.py <this repo>` and flags with `python3 -I tools/build_flag_packs.py <this repo>` from the app repo.
