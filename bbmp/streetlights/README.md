# streetlights

From BBMP tenders issued in 2024 (`BBMP/2024-25/SE0976` and `BBMP/2024-25/SE0979`) as part of *Implementation of Energy Efficiency Project for Streetlights*

* `parse.sh` converts PDFs to CSVs
* `process.sh` inside `Processing/` does basic cleanup and outputs geospatial data

[`Streetlights.fgb`](Processing/Streetlights.fgb) contains the final geospatial data.

### ogrinfo

```
Layer name: Combined
Geometry: Point
Feature Count: 175006
Extent: (7.758690, 1.300940) - (250.000000, 77.673958)
Layer SRS WKT:
GEOGCRS["WGS 84",
    ENSEMBLE["World Geodetic System 1984 ensemble",
        MEMBER["World Geodetic System 1984 (Transit)"],
        MEMBER["World Geodetic System 1984 (G730)"],
        MEMBER["World Geodetic System 1984 (G873)"],
        MEMBER["World Geodetic System 1984 (G1150)"],
        MEMBER["World Geodetic System 1984 (G1674)"],
        MEMBER["World Geodetic System 1984 (G1762)"],
        MEMBER["World Geodetic System 1984 (G2139)"],
        MEMBER["World Geodetic System 1984 (G2296)"],
        ELLIPSOID["WGS 84",6378137,298.257223563,
            LENGTHUNIT["metre",1]],
        ENSEMBLEACCURACY[2.0]],
    PRIMEM["Greenwich",0,
        ANGLEUNIT["degree",0.0174532925199433]],
    CS[ellipsoidal,2],
        AXIS["geodetic latitude (Lat)",north,
            ORDER[1],
            ANGLEUNIT["degree",0.0174532925199433]],
        AXIS["geodetic longitude (Lon)",east,
            ORDER[2],
            ANGLEUNIT["degree",0.0174532925199433]],
    USAGE[
        SCOPE["Horizontal component of 3D system."],
        AREA["World."],
        BBOX[-90,-180,90,180]],
    ID["EPSG",4326]]
Data axis to CRS axis mapping: 2,1
RR No.: String (0.0)
Energy Meter Latitude: String (0.0)
Energy Meter Longitude: String (0.0)
Pole No.: String (0.0)
Pole Latitude: Real (0.0)
Pole Longitude: Real (0.0)
Type: String (0.0)
No. of Lights: String (0.0)
Road Category: String (0.0)
Rated Wattage: String (0.0)
Rated Wattage (Proposed): String (0.0)
```
