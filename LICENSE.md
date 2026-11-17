# Data licenses

Each file is a simplified derivative of the geoBoundaries ADM2 release for its country (Italy uses ADM3). The upstream license for each country carries over to its file:

| File | Source license |
|---|---|
| admin2-AU.geopack | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| admin2-BR.geopack | Creative Commons Attribution 3.0 IGO (CC BY 3.0 IGO) |
| admin2-CA.geopack | Open Government Licence – Canada 2.0 |
| admin2-DE.geopack | Data licence Germany – Attribution – Version 2.0 |
| admin2-ES.geopack | National Institute of Statistics (INE) data license |
| admin2-FR.geopack | Licence Ouverte / Etalab Open License 2.0 |
| admin2-GB.geopack | Open Government Licence v3.0 |
| admin2-IT.geopack | Creative Commons Attribution 3.0 |
| admin2-JP.geopack | Creative Commons Attribution-ShareAlike 2.0 (CC BY-SA 2.0). This derivative is shared under the same license. |
| admin2-MX.geopack | Creative Commons Attribution 4.0 (CC BY 4.0) |

The changes made were: geometry simplification (Douglas-Peucker), reprojection to MapKit map points, and region codes assigned to match ISO 3166-2.

Attribution: geoBoundaries, www.geoboundaries.org.

## Cities

`cities/XX.json` are derived from GeoNames `cities15000` (www.geonames.org), licensed under Creative Commons Attribution 4.0 (CC BY 4.0). The changes made were: places were filtered to cities of 100,000+ people, sorted by population, and tagged with region codes from the app's own outlines.
