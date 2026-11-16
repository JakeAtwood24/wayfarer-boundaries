# Wayfarer Journal: district boundaries

These are simplified county-level (admin-2) boundaries, one file per country. The Wayfarer Journal iOS app downloads them when someone opens that country's Districts layer.

- `manifest.json` lists each file with its size, SHA-256 checksum, data version (`v`) and source license.
- `admin2-XX.geopack` files are a binary format: a JSON metadata header followed by MKMapPoint coordinate pairs. They are built by `tools/geobuild.swift` in the app's repository.

All files are derived from [geoBoundaries](https://www.geoboundaries.org) (Runfola et al., 2020, *geoBoundaries: A global database of political administrative boundaries*, PLoS ONE 15(4): e0231866).

See [LICENSE.md](LICENSE.md) for the license of each country's data.
