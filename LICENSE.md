# Data licenses

Each file is a simplified derivative of the geoBoundaries ADM2 release for its country (Italy uses ADM3). The upstream license for each country carries over to its file:

| File | Source license |
|---|---|
| admin2-AT.geopack | Creative Commons Attribution-ShareAlike 2.0 |
| admin2-SA.geopack | Creative Commons Attribution-ShareAlike 2.0 |
| admin2-MX.geopack | Creative Commons Attribution 4.0 (CC BY 4.0) |
| admin2-TR.geopack | Open Data Commons Open Database License 1.0 |
| admin2-TH.geopack | Creative Commons Attribution 3.0 Intergovernmental Organisations (CC BY 3.0 IGO) |
| admin2-PT.geopack | CC0 1.0 Universal (CC0 1.0) Public Domain Dedication |
| admin2-GR.geopack | CC0 1.0 Universal (CC0 1.0) Public Domain Dedication |
| admin2-ES.geopack | National Institute of Statistics (INE) Data License |
| admin2-FR.geopack | Etalab Open License 2.0 |
| admin2-IT.geopack | Creative Commons Attribution 3.0 License |
| admin2-GB.geopack | Open Government Licence v3.0 |
| admin2-DE.geopack | Data license Germany - Attribution - Version 2.0 |
| admin2-CA.geopack | Open Government Canada 2.0 |
| admin2-JP.geopack | Creative Commons Attribution-ShareAlike 2.0 |
| admin2-AU.geopack | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| admin2-BR.geopack | Creative Commons Attribution 3.0 Intergovernmental Organisations (CC BY 3.0 IGO) |

The changes made were: geometry simplification (Douglas-Peucker), reprojection to MapKit map points, and region codes assigned to match ISO 3166-2.

Attribution: geoBoundaries, www.geoboundaries.org.

## Cities

`cities/XX.json` are derived from GeoNames `cities15000` (www.geonames.org), licensed under Creative Commons Attribution 4.0 (CC BY 4.0). The changes made were: places were filtered to cities of 100,000+ people, sorted by population, and tagged with region codes from the app's own outlines.
