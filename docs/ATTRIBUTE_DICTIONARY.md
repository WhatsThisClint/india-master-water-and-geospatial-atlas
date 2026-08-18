# Comprehensive Master Attribute Dictionary

> **Consolidated Database**: `india_master_water_and_geospatial_atlas.gpkg`
> **Total Documented Attributes**: 703 Columns

---

## Table-by-Table Attribute Specifications


### Table: `assembly_constituencies_vidhan_sabha`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for assembly_constituencies_vidhan_sabha. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for assembly_constituencies_vidhan_sabha. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`OBJECTID`** | `int64` | Dimensionless / Text | No | Attribute field 'OBJECTID' representing record properties in Vidhan Sabha State Assembly Constituencies. | Inspect 'OBJECTID' values for querying and filtering features in Vidhan Sabha State Assembly Constituencies. |
| **`ST_CODE`** | `int64` | Dimensionless / Text | No | Attribute field 'ST_CODE' representing record properties in Vidhan Sabha State Assembly Constituencies. | Inspect 'ST_CODE' values for querying and filtering features in Vidhan Sabha State Assembly Constituencies. |
| **`ST_NAME`** | `str` | Dimensionless / Text | ⭐ Yes | Attribute field 'ST_NAME' representing record properties in Vidhan Sabha State Assembly Constituencies. | Inspect 'ST_NAME' values for querying and filtering features in Vidhan Sabha State Assembly Constituencies. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of Vidhan Sabha State Assembly Constituencies). |
| **`DT_CODE`** | `float64` | Dimensionless / Text | No | Attribute field 'DT_CODE' representing record properties in Vidhan Sabha State Assembly Constituencies. | Inspect 'DT_CODE' values for querying and filtering features in Vidhan Sabha State Assembly Constituencies. |
| **`DIST_NAME`** | `str` | Dimensionless / Text | No | Attribute field 'DIST_NAME' representing record properties in Vidhan Sabha State Assembly Constituencies. | Inspect 'DIST_NAME' values for querying and filtering features in Vidhan Sabha State Assembly Constituencies. |
| **`AC_NO`** | `int64` | Integer | No | Assembly Constituency number within the state. | Constituency serial number. |
| **`AC_NAME`** | `str` | Text | No | Name of the State Vidhan Sabha Legislative Assembly Constituency. | e.g., Tizit, Tapi, Chandni Chowk. |
| **`PC_NO`** | `int64` | Dimensionless / Text | No | Attribute field 'PC_NO' representing record properties in Vidhan Sabha State Assembly Constituencies. | Inspect 'PC_NO' values for querying and filtering features in Vidhan Sabha State Assembly Constituencies. |
| **`PC_NAME`** | `str` | Dimensionless / Text | No | Attribute field 'PC_NAME' representing record properties in Vidhan Sabha State Assembly Constituencies. | Inspect 'PC_NAME' values for querying and filtering features in Vidhan Sabha State Assembly Constituencies. |
| **`PC_ID`** | `int64` | Dimensionless / Text | No | Attribute field 'PC_ID' representing record properties in Vidhan Sabha State Assembly Constituencies. | Inspect 'PC_ID' values for querying and filtering features in Vidhan Sabha State Assembly Constituencies. |
| **`STATUS`** | `str` | Dimensionless / Text | No | Attribute field 'STATUS' representing record properties in Vidhan Sabha State Assembly Constituencies. | Inspect 'STATUS' values for querying and filtering features in Vidhan Sabha State Assembly Constituencies. |
| **`Shape_Leng`** | `float64` | Dimensionless / Text | No | Attribute field 'Shape_Leng' representing record properties in Vidhan Sabha State Assembly Constituencies. | Inspect 'Shape_Leng' values for querying and filtering features in Vidhan Sabha State Assembly Constituencies. |
| **`Shape_Area`** | `float64` | Dimensionless / Text | No | Attribute field 'Shape_Area' representing record properties in Vidhan Sabha State Assembly Constituencies. | Inspect 'Shape_Area' values for querying and filtering features in Vidhan Sabha State Assembly Constituencies. |

### Table: `geopackage_data_india_geoportal_layers_india_populated_places`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for geopackage_data_india_geoportal_layers_india_populated_places. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for geopackage_data_india_geoportal_layers_india_populated_places. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`SCALERANK`** | `int64` | Dimensionless / Text | No | Attribute field 'SCALERANK' representing record properties in Major Populated Places & Cities. | Inspect 'SCALERANK' values for querying and filtering features in Major Populated Places & Cities. |
| **`NATSCALE`** | `int64` | Dimensionless / Text | No | Attribute field 'NATSCALE' representing record properties in Major Populated Places & Cities. | Inspect 'NATSCALE' values for querying and filtering features in Major Populated Places & Cities. |
| **`LABELRANK`** | `float64` | Dimensionless / Text | No | Attribute field 'LABELRANK' representing record properties in Major Populated Places & Cities. | Inspect 'LABELRANK' values for querying and filtering features in Major Populated Places & Cities. |
| **`FEATURECLA`** | `str` | Dimensionless / Text | No | Attribute field 'FEATURECLA' representing record properties in Major Populated Places & Cities. | Inspect 'FEATURECLA' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME`** | `str` | Dimensionless / Text | No | Attribute field 'NAME' representing record properties in Major Populated Places & Cities. | Inspect 'NAME' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAMEPAR`** | `object` | Dimensionless / Text | No | Attribute field 'NAMEPAR' representing record properties in Major Populated Places & Cities. | Inspect 'NAMEPAR' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAMEALT`** | `str` | Dimensionless / Text | No | Attribute field 'NAMEALT' representing record properties in Major Populated Places & Cities. | Inspect 'NAMEALT' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAMEASCII`** | `str` | Dimensionless / Text | No | Attribute field 'NAMEASCII' representing record properties in Major Populated Places & Cities. | Inspect 'NAMEASCII' values for querying and filtering features in Major Populated Places & Cities. |
| **`ADM0CAP`** | `int64` | Dimensionless / Text | No | Attribute field 'ADM0CAP' representing record properties in Major Populated Places & Cities. | Inspect 'ADM0CAP' values for querying and filtering features in Major Populated Places & Cities. |
| **`CAPIN`** | `object` | Dimensionless / Text | No | Attribute field 'CAPIN' representing record properties in Major Populated Places & Cities. | Inspect 'CAPIN' values for querying and filtering features in Major Populated Places & Cities. |
| **`WORLDCITY`** | `int64` | Dimensionless / Text | No | Attribute field 'WORLDCITY' representing record properties in Major Populated Places & Cities. | Inspect 'WORLDCITY' values for querying and filtering features in Major Populated Places & Cities. |
| **`MEGACITY`** | `int64` | Dimensionless / Text | No | Attribute field 'MEGACITY' representing record properties in Major Populated Places & Cities. | Inspect 'MEGACITY' values for querying and filtering features in Major Populated Places & Cities. |
| **`SOV0NAME`** | `str` | Dimensionless / Text | No | Attribute field 'SOV0NAME' representing record properties in Major Populated Places & Cities. | Inspect 'SOV0NAME' values for querying and filtering features in Major Populated Places & Cities. |
| **`SOV_A3`** | `str` | Dimensionless / Text | No | Attribute field 'SOV_A3' representing record properties in Major Populated Places & Cities. | Inspect 'SOV_A3' values for querying and filtering features in Major Populated Places & Cities. |
| **`ADM0NAME`** | `str` | Dimensionless / Text | No | Attribute field 'ADM0NAME' representing record properties in Major Populated Places & Cities. | Inspect 'ADM0NAME' values for querying and filtering features in Major Populated Places & Cities. |
| **`ADM0_A3`** | `str` | Dimensionless / Text | No | Attribute field 'ADM0_A3' representing record properties in Major Populated Places & Cities. | Inspect 'ADM0_A3' values for querying and filtering features in Major Populated Places & Cities. |
| **`ADM1NAME`** | `str` | Dimensionless / Text | No | Attribute field 'ADM1NAME' representing record properties in Major Populated Places & Cities. | Inspect 'ADM1NAME' values for querying and filtering features in Major Populated Places & Cities. |
| **`ISO_A2`** | `str` | Dimensionless / Text | No | Attribute field 'ISO_A2' representing record properties in Major Populated Places & Cities. | Inspect 'ISO_A2' values for querying and filtering features in Major Populated Places & Cities. |
| **`NOTE`** | `object` | Dimensionless / Text | No | Attribute field 'NOTE' representing record properties in Major Populated Places & Cities. | Inspect 'NOTE' values for querying and filtering features in Major Populated Places & Cities. |
| **`LATITUDE`** | `float64` | Dimensionless / Text | No | Attribute field 'LATITUDE' representing record properties in Major Populated Places & Cities. | Inspect 'LATITUDE' values for querying and filtering features in Major Populated Places & Cities. |
| **`LONGITUDE`** | `float64` | Dimensionless / Text | No | Attribute field 'LONGITUDE' representing record properties in Major Populated Places & Cities. | Inspect 'LONGITUDE' values for querying and filtering features in Major Populated Places & Cities. |
| **`POP_MAX`** | `int64` | Persons (Count) | ⭐ Yes | Maximum estimated urban agglomeration population for the city / populated place. | Urban water consumption modeling and municipal water supply infrastructure sizing. |
| **`POP_MIN`** | `int64` | Persons (Count) | No | Minimum core municipal population count. | Municipal core population baseline. |
| **`POP_OTHER`** | `float64` | Dimensionless / Text | No | Attribute field 'POP_OTHER' representing record properties in Major Populated Places & Cities. | Inspect 'POP_OTHER' values for querying and filtering features in Major Populated Places & Cities. |
| **`RANK_MAX`** | `int64` | Dimensionless / Text | No | Attribute field 'RANK_MAX' representing record properties in Major Populated Places & Cities. | Inspect 'RANK_MAX' values for querying and filtering features in Major Populated Places & Cities. |
| **`RANK_MIN`** | `int64` | Dimensionless / Text | No | Attribute field 'RANK_MIN' representing record properties in Major Populated Places & Cities. | Inspect 'RANK_MIN' values for querying and filtering features in Major Populated Places & Cities. |
| **`MEGANAME`** | `object` | Dimensionless / Text | No | Attribute field 'MEGANAME' representing record properties in Major Populated Places & Cities. | Inspect 'MEGANAME' values for querying and filtering features in Major Populated Places & Cities. |
| **`LS_NAME`** | `str` | Dimensionless / Text | No | Attribute field 'LS_NAME' representing record properties in Major Populated Places & Cities. | Inspect 'LS_NAME' values for querying and filtering features in Major Populated Places & Cities. |
| **`MAX_POP10`** | `float64` | Dimensionless / Text | No | Attribute field 'MAX_POP10' representing record properties in Major Populated Places & Cities. | Inspect 'MAX_POP10' values for querying and filtering features in Major Populated Places & Cities. |
| **`MAX_POP20`** | `float64` | Dimensionless / Text | No | Attribute field 'MAX_POP20' representing record properties in Major Populated Places & Cities. | Inspect 'MAX_POP20' values for querying and filtering features in Major Populated Places & Cities. |
| **`MAX_POP50`** | `float64` | Dimensionless / Text | No | Attribute field 'MAX_POP50' representing record properties in Major Populated Places & Cities. | Inspect 'MAX_POP50' values for querying and filtering features in Major Populated Places & Cities. |
| **`MAX_POP300`** | `float64` | Dimensionless / Text | No | Attribute field 'MAX_POP300' representing record properties in Major Populated Places & Cities. | Inspect 'MAX_POP300' values for querying and filtering features in Major Populated Places & Cities. |
| **`MAX_POP310`** | `float64` | Dimensionless / Text | No | Attribute field 'MAX_POP310' representing record properties in Major Populated Places & Cities. | Inspect 'MAX_POP310' values for querying and filtering features in Major Populated Places & Cities. |
| **`MAX_NATSCA`** | `float64` | Dimensionless / Text | No | Attribute field 'MAX_NATSCA' representing record properties in Major Populated Places & Cities. | Inspect 'MAX_NATSCA' values for querying and filtering features in Major Populated Places & Cities. |
| **`MIN_AREAKM`** | `float64` | Dimensionless / Text | No | Attribute field 'MIN_AREAKM' representing record properties in Major Populated Places & Cities. | Inspect 'MIN_AREAKM' values for querying and filtering features in Major Populated Places & Cities. |
| **`MAX_AREAKM`** | `float64` | Dimensionless / Text | No | Attribute field 'MAX_AREAKM' representing record properties in Major Populated Places & Cities. | Inspect 'MAX_AREAKM' values for querying and filtering features in Major Populated Places & Cities. |
| **`MIN_AREAMI`** | `float64` | Dimensionless / Text | No | Attribute field 'MIN_AREAMI' representing record properties in Major Populated Places & Cities. | Inspect 'MIN_AREAMI' values for querying and filtering features in Major Populated Places & Cities. |
| **`MAX_AREAMI`** | `float64` | Dimensionless / Text | No | Attribute field 'MAX_AREAMI' representing record properties in Major Populated Places & Cities. | Inspect 'MAX_AREAMI' values for querying and filtering features in Major Populated Places & Cities. |
| **`MIN_PERKM`** | `float64` | Dimensionless / Text | No | Attribute field 'MIN_PERKM' representing record properties in Major Populated Places & Cities. | Inspect 'MIN_PERKM' values for querying and filtering features in Major Populated Places & Cities. |
| **`MAX_PERKM`** | `float64` | Dimensionless / Text | No | Attribute field 'MAX_PERKM' representing record properties in Major Populated Places & Cities. | Inspect 'MAX_PERKM' values for querying and filtering features in Major Populated Places & Cities. |
| **`MIN_PERMI`** | `float64` | Dimensionless / Text | No | Attribute field 'MIN_PERMI' representing record properties in Major Populated Places & Cities. | Inspect 'MIN_PERMI' values for querying and filtering features in Major Populated Places & Cities. |
| **`MAX_PERMI`** | `float64` | Dimensionless / Text | No | Attribute field 'MAX_PERMI' representing record properties in Major Populated Places & Cities. | Inspect 'MAX_PERMI' values for querying and filtering features in Major Populated Places & Cities. |
| **`MIN_BBXMIN`** | `float64` | Dimensionless / Text | No | Attribute field 'MIN_BBXMIN' representing record properties in Major Populated Places & Cities. | Inspect 'MIN_BBXMIN' values for querying and filtering features in Major Populated Places & Cities. |
| **`MAX_BBXMIN`** | `float64` | Dimensionless / Text | No | Attribute field 'MAX_BBXMIN' representing record properties in Major Populated Places & Cities. | Inspect 'MAX_BBXMIN' values for querying and filtering features in Major Populated Places & Cities. |
| **`MIN_BBXMAX`** | `float64` | Dimensionless / Text | No | Attribute field 'MIN_BBXMAX' representing record properties in Major Populated Places & Cities. | Inspect 'MIN_BBXMAX' values for querying and filtering features in Major Populated Places & Cities. |
| **`MAX_BBXMAX`** | `float64` | Dimensionless / Text | No | Attribute field 'MAX_BBXMAX' representing record properties in Major Populated Places & Cities. | Inspect 'MAX_BBXMAX' values for querying and filtering features in Major Populated Places & Cities. |
| **`MIN_BBYMIN`** | `float64` | Dimensionless / Text | No | Attribute field 'MIN_BBYMIN' representing record properties in Major Populated Places & Cities. | Inspect 'MIN_BBYMIN' values for querying and filtering features in Major Populated Places & Cities. |
| **`MAX_BBYMIN`** | `float64` | Dimensionless / Text | No | Attribute field 'MAX_BBYMIN' representing record properties in Major Populated Places & Cities. | Inspect 'MAX_BBYMIN' values for querying and filtering features in Major Populated Places & Cities. |
| **`MIN_BBYMAX`** | `float64` | Dimensionless / Text | No | Attribute field 'MIN_BBYMAX' representing record properties in Major Populated Places & Cities. | Inspect 'MIN_BBYMAX' values for querying and filtering features in Major Populated Places & Cities. |
| **`MAX_BBYMAX`** | `float64` | Dimensionless / Text | No | Attribute field 'MAX_BBYMAX' representing record properties in Major Populated Places & Cities. | Inspect 'MAX_BBYMAX' values for querying and filtering features in Major Populated Places & Cities. |
| **`MEAN_BBXC`** | `float64` | Dimensionless / Text | No | Attribute field 'MEAN_BBXC' representing record properties in Major Populated Places & Cities. | Inspect 'MEAN_BBXC' values for querying and filtering features in Major Populated Places & Cities. |
| **`MEAN_BBYC`** | `float64` | Dimensionless / Text | No | Attribute field 'MEAN_BBYC' representing record properties in Major Populated Places & Cities. | Inspect 'MEAN_BBYC' values for querying and filtering features in Major Populated Places & Cities. |
| **`TIMEZONE`** | `str` | Dimensionless / Text | No | Attribute field 'TIMEZONE' representing record properties in Major Populated Places & Cities. | Inspect 'TIMEZONE' values for querying and filtering features in Major Populated Places & Cities. |
| **`UN_FID`** | `float64` | Dimensionless / Text | No | Attribute field 'UN_FID' representing record properties in Major Populated Places & Cities. | Inspect 'UN_FID' values for querying and filtering features in Major Populated Places & Cities. |
| **`POP1950`** | `float64` | Dimensionless / Text | No | Attribute field 'POP1950' representing record properties in Major Populated Places & Cities. | Inspect 'POP1950' values for querying and filtering features in Major Populated Places & Cities. |
| **`POP1955`** | `float64` | Dimensionless / Text | No | Attribute field 'POP1955' representing record properties in Major Populated Places & Cities. | Inspect 'POP1955' values for querying and filtering features in Major Populated Places & Cities. |
| **`POP1960`** | `float64` | Dimensionless / Text | No | Attribute field 'POP1960' representing record properties in Major Populated Places & Cities. | Inspect 'POP1960' values for querying and filtering features in Major Populated Places & Cities. |
| **`POP1965`** | `float64` | Dimensionless / Text | No | Attribute field 'POP1965' representing record properties in Major Populated Places & Cities. | Inspect 'POP1965' values for querying and filtering features in Major Populated Places & Cities. |
| **`POP1970`** | `float64` | Dimensionless / Text | No | Attribute field 'POP1970' representing record properties in Major Populated Places & Cities. | Inspect 'POP1970' values for querying and filtering features in Major Populated Places & Cities. |
| **`POP1975`** | `float64` | Dimensionless / Text | No | Attribute field 'POP1975' representing record properties in Major Populated Places & Cities. | Inspect 'POP1975' values for querying and filtering features in Major Populated Places & Cities. |
| **`POP1980`** | `float64` | Dimensionless / Text | No | Attribute field 'POP1980' representing record properties in Major Populated Places & Cities. | Inspect 'POP1980' values for querying and filtering features in Major Populated Places & Cities. |
| **`POP1985`** | `float64` | Dimensionless / Text | No | Attribute field 'POP1985' representing record properties in Major Populated Places & Cities. | Inspect 'POP1985' values for querying and filtering features in Major Populated Places & Cities. |
| **`POP1990`** | `float64` | Dimensionless / Text | No | Attribute field 'POP1990' representing record properties in Major Populated Places & Cities. | Inspect 'POP1990' values for querying and filtering features in Major Populated Places & Cities. |
| **`POP1995`** | `float64` | Dimensionless / Text | No | Attribute field 'POP1995' representing record properties in Major Populated Places & Cities. | Inspect 'POP1995' values for querying and filtering features in Major Populated Places & Cities. |
| **`POP2000`** | `float64` | Persons (Count) | No | Historical city population in Year 2000. | 20-year urban growth trajectory baseline. |
| **`POP2005`** | `float64` | Dimensionless / Text | No | Attribute field 'POP2005' representing record properties in Major Populated Places & Cities. | Inspect 'POP2005' values for querying and filtering features in Major Populated Places & Cities. |
| **`POP2010`** | `float64` | Persons (Count) | No | Historical city population in Year 2010. | Decadal urban growth midpoint. |
| **`POP2015`** | `float64` | Dimensionless / Text | No | Attribute field 'POP2015' representing record properties in Major Populated Places & Cities. | Inspect 'POP2015' values for querying and filtering features in Major Populated Places & Cities. |
| **`POP2020`** | `float64` | Persons (Count) | ⭐ Yes | Estimated city population in Year 2020. | Current urban water demand modeling. |
| **`POP2025`** | `float64` | Dimensionless / Text | No | Attribute field 'POP2025' representing record properties in Major Populated Places & Cities. | Inspect 'POP2025' values for querying and filtering features in Major Populated Places & Cities. |
| **`POP2050`** | `float64` | Persons (Count) | ⭐ Yes | Long-term projected urban population in Year 2050. | Future-proofing major dam reservoirs and long-distance inter-basin water transfer projects. |
| **`MIN_ZOOM`** | `float64` | Dimensionless / Text | No | Attribute field 'MIN_ZOOM' representing record properties in Major Populated Places & Cities. | Inspect 'MIN_ZOOM' values for querying and filtering features in Major Populated Places & Cities. |
| **`WIKIDATAID`** | `str` | Dimensionless / Text | No | Attribute field 'WIKIDATAID' representing record properties in Major Populated Places & Cities. | Inspect 'WIKIDATAID' values for querying and filtering features in Major Populated Places & Cities. |
| **`WOF_ID`** | `int64` | Dimensionless / Text | No | Attribute field 'WOF_ID' representing record properties in Major Populated Places & Cities. | Inspect 'WOF_ID' values for querying and filtering features in Major Populated Places & Cities. |
| **`CAPALT`** | `int64` | Dimensionless / Text | No | Attribute field 'CAPALT' representing record properties in Major Populated Places & Cities. | Inspect 'CAPALT' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_EN`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_EN' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_EN' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_DE`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_DE' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_DE' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_ES`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_ES' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_ES' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_FR`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_FR' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_FR' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_PT`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_PT' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_PT' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_RU`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_RU' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_RU' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_ZH`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_ZH' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_ZH' values for querying and filtering features in Major Populated Places & Cities. |
| **`LABEL`** | `str` | Dimensionless / Text | No | Attribute field 'LABEL' representing record properties in Major Populated Places & Cities. | Inspect 'LABEL' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_AR`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_AR' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_AR' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_BN`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_BN' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_BN' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_EL`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_EL' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_EL' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_HI`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_HI' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_HI' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_HU`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_HU' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_HU' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_ID`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_ID' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_ID' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_IT`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_IT' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_IT' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_JA`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_JA' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_JA' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_KO`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_KO' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_KO' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_NL`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_NL' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_NL' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_PL`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_PL' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_PL' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_SV`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_SV' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_SV' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_TR`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_TR' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_TR' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_VI`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_VI' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_VI' values for querying and filtering features in Major Populated Places & Cities. |
| **`NE_ID`** | `int64` | Dimensionless / Text | No | Attribute field 'NE_ID' representing record properties in Major Populated Places & Cities. | Inspect 'NE_ID' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_FA`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_FA' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_FA' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_HE`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_HE' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_HE' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_UK`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_UK' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_UK' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_UR`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_UR' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_UR' values for querying and filtering features in Major Populated Places & Cities. |
| **`NAME_ZHT`** | `str` | Dimensionless / Text | No | Attribute field 'NAME_ZHT' representing record properties in Major Populated Places & Cities. | Inspect 'NAME_ZHT' values for querying and filtering features in Major Populated Places & Cities. |
| **`GEONAMESID`** | `float64` | Dimensionless / Text | No | Attribute field 'GEONAMESID' representing record properties in Major Populated Places & Cities. | Inspect 'GEONAMESID' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_ISO`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_ISO' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_ISO' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_US`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_US' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_US' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_FR`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_FR' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_FR' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_RU`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_RU' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_RU' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_ES`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_ES' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_ES' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_CN`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_CN' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_CN' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_TW`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_TW' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_TW' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_IN`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_IN' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_IN' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_NP`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_NP' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_NP' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_PK`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_PK' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_PK' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_DE`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_DE' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_DE' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_GB`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_GB' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_GB' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_BR`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_BR' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_BR' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_IL`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_IL' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_IL' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_PS`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_PS' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_PS' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_SA`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_SA' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_SA' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_EG`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_EG' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_EG' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_MA`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_MA' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_MA' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_PT`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_PT' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_PT' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_AR`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_AR' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_AR' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_JP`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_JP' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_JP' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_KO`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_KO' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_KO' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_VN`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_VN' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_VN' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_TR`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_TR' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_TR' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_ID`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_ID' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_ID' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_PL`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_PL' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_PL' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_GR`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_GR' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_GR' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_IT`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_IT' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_IT' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_NL`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_NL' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_NL' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_SE`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_SE' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_SE' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_BD`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_BD' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_BD' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_UA`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_UA' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_UA' values for querying and filtering features in Major Populated Places & Cities. |
| **`FCLASS_TLC`** | `object` | Dimensionless / Text | No | Attribute field 'FCLASS_TLC' representing record properties in Major Populated Places & Cities. | Inspect 'FCLASS_TLC' values for querying and filtering features in Major Populated Places & Cities. |

### Table: `geopackage_data_india_geoportal_layers_india_ports`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for geopackage_data_india_geoportal_layers_india_ports. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for geopackage_data_india_geoportal_layers_india_ports. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`scalerank`** | `int64` | Dimensionless / Text | No | Attribute field 'scalerank' representing record properties in Major Ports & Harbours of India. | Inspect 'scalerank' values for querying and filtering features in Major Ports & Harbours of India. |
| **`featurecla`** | `str` | Categorical | No | Natural Earth / Open Portal geographic feature classification. | Admin-0 capital (national capital), Admin-1 capital (state capital), Populated place (major city), River, Port. |
| **`name`** | `str` | Dimensionless / Text | No | Attribute field 'name' representing record properties in Major Ports & Harbours of India. | Inspect 'name' values for querying and filtering features in Major Ports & Harbours of India. |
| **`website`** | `str` | Dimensionless / Text | No | Attribute field 'website' representing record properties in Major Ports & Harbours of India. | Inspect 'website' values for querying and filtering features in Major Ports & Harbours of India. |
| **`natlscale`** | `int64` | Dimensionless / Text | No | Attribute field 'natlscale' representing record properties in Major Ports & Harbours of India. | Inspect 'natlscale' values for querying and filtering features in Major Ports & Harbours of India. |
| **`ne_id`** | `int64` | Dimensionless / Text | No | Attribute field 'ne_id' representing record properties in Major Ports & Harbours of India. | Inspect 'ne_id' values for querying and filtering features in Major Ports & Harbours of India. |

### Table: `geopackage_data_india_geoportal_layers_india_wris_water_project`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for geopackage_data_india_geoportal_layers_india_wris_water_project. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for geopackage_data_india_geoportal_layers_india_wris_water_project. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`objectid`** | `int64` | Dimensionless / Text | No | Attribute field 'objectid' representing record properties in India WRIS Water Resources Projects. | Inspect 'objectid' values for querying and filtering features in India WRIS Water Resources Projects. |
| **`ph_name`** | `str` | Text | No | Official project name of the water resource asset (Dam, Barrage, Reservoir, Lift Scheme). | e.g., Bhakra Nangal, Hirakud, Nagarjuna Sagar, Sardar Sarovar. |
| **`phcode`** | `str` | Dimensionless / Text | No | Attribute field 'phcode' representing record properties in India WRIS Water Resources Projects. | Inspect 'phcode' values for querying and filtering features in India WRIS Water Resources Projects. |
| **`class`** | `str` | Categorical | No | Detailed functional class tag. | power_line, breakwater, generator, power_tower, toll_booth. |
| **`ltype`** | `str` | Dimensionless / Text | No | Attribute field 'ltype' representing record properties in India WRIS Water Resources Projects. | Inspect 'ltype' values for querying and filtering features in India WRIS Water Resources Projects. |
| **`ph_pw_loca`** | `str` | Dimensionless / Text | No | Attribute field 'ph_pw_loca' representing record properties in India WRIS Water Resources Projects. | Inspect 'ph_pw_loca' values for querying and filtering features in India WRIS Water Resources Projects. |
| **`ph_type`** | `str` | Categorical | No | Type of water infrastructure project. | Major Irrigation Project, Medium Irrigation Project, Hydro Electric Project, Lift Irrigation Scheme, Dam/Barrage. |
| **`ph_com_yr`** | `float64` | Dimensionless / Text | No | Attribute field 'ph_com_yr' representing record properties in India WRIS Water Resources Projects. | Inspect 'ph_com_yr' values for querying and filtering features in India WRIS Water Resources Projects. |
| **`ph_pw_totcap`** | `float64` | Megawatts (MW) / MCM | No | Total power generation capacity or storage reservoir capacity. | Capacity metric for hydro power and storage. |
| **`ph_pw_ade`** | `float64` | Dimensionless / Text | No | Attribute field 'ph_pw_ade' representing record properties in India WRIS Water Resources Projects. | Inspect 'ph_pw_ade' values for querying and filtering features in India WRIS Water Resources Projects. |
| **`state`** | `str` | Text | No | State where the water project is located. | State location. |
| **`bacode`** | `object` | Dimensionless / Text | No | Attribute field 'bacode' representing record properties in India WRIS Water Resources Projects. | Inspect 'bacode' values for querying and filtering features in India WRIS Water Resources Projects. |

### Table: `hydrobasins_asia_level_1`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_1. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_1. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYBAS_ID`** | `int64` | Identifier | No | Unique HydroBASINS polygon feature identifier (Pfafstetter hierarchical ID). | Use as primary key for topological basin joins and hierarchical tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`NEXT_SINK`** | `int64` | Identifier | No | HYBAS_ID of the final coastal sink or endorheic inland terminal basin. | Group by NEXT_SINK to identify all basins contributing to a common river mouth or delta. |
| **`MAIN_BAS`** | `int64` | Identifier | No | HYBAS_ID of the overall primary river basin system (e.g., Ganga, Indus, Godavari). | Filter by MAIN_BAS to isolate all sub-basins belonging to a major national river basin. |
| **`DIST_SINK`** | `float64` | Kilometers (km) | No | Distance along the flow path from the basin outlet to the final coastal or terminal sink. | Use for flow travel time and routing delay estimations. |
| **`DIST_MAIN`** | `float64` | Kilometers (km) | No | Distance along the mainstem river channel from the basin outlet to the ocean sink. | Use for river network longitudinal distance calculations. |
| **`SUB_AREA`** | `float64` | Square Kilometers (km²) | ⭐ Yes | Local surface area of this individual sub-basin polygon. | Sum local SUB_AREA or calculate local precipitation volume = SUB_AREA * rainfall. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroBASINS Level 1 (Continental Basins)). |
| **`UP_AREA`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream drainage area contributing flow through this basin outlet. | UP_AREA > 10,000 indicates major river mainstems; use to distinguish headwaters from main channels. |
| **`PFAF_ID`** | `int64` | Pfafstetter Code | No | Topological Pfafstetter drainage code encoding stream hierarchy and basin topology. | Digits from left to right represent nested basin hierarchy from continental level to micro level. |
| **`ENDO`** | `int64` | Flag (0 or 1) | No | Endorheic indicator flag: 1 = basin drains to an inland sink/lake with no outlet to the ocean, 0 = exorheic. | 1 indicates closed inland basins (e.g., Sambhar Lake basin in Rajasthan, Ladakh sinks). |
| **`COAST`** | `int64` | Flag (0 or 1) | No | Coastal basin indicator flag: 1 = basin directly touches the coastline, 0 = inland basin. | Filter COAST = 1 to analyze coastal estuaries, backwaters, and sea-level rise vulnerability. |
| **`ORDER`** | `int64` | Integer Rank | No | Hydrological stream ordering of the main drainage reach within the basin. | Higher numbers represent higher order channels. |
| **`SORT`** | `int64` | Integer | No | Topological sorting sequence ensuring downstream basins have higher sort values. | Sort ascending by SORT to process basins in upstream-to-downstream order. |

### Table: `hydrobasins_asia_level_10`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_10. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_10. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYBAS_ID`** | `int64` | Identifier | No | Unique HydroBASINS polygon feature identifier (Pfafstetter hierarchical ID). | Use as primary key for topological basin joins and hierarchical tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`NEXT_SINK`** | `int64` | Identifier | No | HYBAS_ID of the final coastal sink or endorheic inland terminal basin. | Group by NEXT_SINK to identify all basins contributing to a common river mouth or delta. |
| **`MAIN_BAS`** | `int64` | Identifier | No | HYBAS_ID of the overall primary river basin system (e.g., Ganga, Indus, Godavari). | Filter by MAIN_BAS to isolate all sub-basins belonging to a major national river basin. |
| **`DIST_SINK`** | `float64` | Kilometers (km) | No | Distance along the flow path from the basin outlet to the final coastal or terminal sink. | Use for flow travel time and routing delay estimations. |
| **`DIST_MAIN`** | `float64` | Kilometers (km) | No | Distance along the mainstem river channel from the basin outlet to the ocean sink. | Use for river network longitudinal distance calculations. |
| **`SUB_AREA`** | `float64` | Square Kilometers (km²) | ⭐ Yes | Local surface area of this individual sub-basin polygon. | Sum local SUB_AREA or calculate local precipitation volume = SUB_AREA * rainfall. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroBASINS Level 10 (Micro-catchments)). |
| **`UP_AREA`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream drainage area contributing flow through this basin outlet. | UP_AREA > 10,000 indicates major river mainstems; use to distinguish headwaters from main channels. |
| **`PFAF_ID`** | `int64` | Pfafstetter Code | No | Topological Pfafstetter drainage code encoding stream hierarchy and basin topology. | Digits from left to right represent nested basin hierarchy from continental level to micro level. |
| **`ENDO`** | `int64` | Flag (0 or 1) | No | Endorheic indicator flag: 1 = basin drains to an inland sink/lake with no outlet to the ocean, 0 = exorheic. | 1 indicates closed inland basins (e.g., Sambhar Lake basin in Rajasthan, Ladakh sinks). |
| **`COAST`** | `int64` | Flag (0 or 1) | No | Coastal basin indicator flag: 1 = basin directly touches the coastline, 0 = inland basin. | Filter COAST = 1 to analyze coastal estuaries, backwaters, and sea-level rise vulnerability. |
| **`ORDER`** | `int64` | Integer Rank | No | Hydrological stream ordering of the main drainage reach within the basin. | Higher numbers represent higher order channels. |
| **`SORT`** | `int64` | Integer | No | Topological sorting sequence ensuring downstream basins have higher sort values. | Sort ascending by SORT to process basins in upstream-to-downstream order. |

### Table: `hydrobasins_asia_level_11`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_11. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_11. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYBAS_ID`** | `int64` | Identifier | No | Unique HydroBASINS polygon feature identifier (Pfafstetter hierarchical ID). | Use as primary key for topological basin joins and hierarchical tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`NEXT_SINK`** | `int64` | Identifier | No | HYBAS_ID of the final coastal sink or endorheic inland terminal basin. | Group by NEXT_SINK to identify all basins contributing to a common river mouth or delta. |
| **`MAIN_BAS`** | `int64` | Identifier | No | HYBAS_ID of the overall primary river basin system (e.g., Ganga, Indus, Godavari). | Filter by MAIN_BAS to isolate all sub-basins belonging to a major national river basin. |
| **`DIST_SINK`** | `float64` | Kilometers (km) | No | Distance along the flow path from the basin outlet to the final coastal or terminal sink. | Use for flow travel time and routing delay estimations. |
| **`DIST_MAIN`** | `float64` | Kilometers (km) | No | Distance along the mainstem river channel from the basin outlet to the ocean sink. | Use for river network longitudinal distance calculations. |
| **`SUB_AREA`** | `float64` | Square Kilometers (km²) | ⭐ Yes | Local surface area of this individual sub-basin polygon. | Sum local SUB_AREA or calculate local precipitation volume = SUB_AREA * rainfall. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroBASINS Level 11 (Sub-microwatersheds)). |
| **`UP_AREA`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream drainage area contributing flow through this basin outlet. | UP_AREA > 10,000 indicates major river mainstems; use to distinguish headwaters from main channels. |
| **`PFAF_ID`** | `int64` | Pfafstetter Code | No | Topological Pfafstetter drainage code encoding stream hierarchy and basin topology. | Digits from left to right represent nested basin hierarchy from continental level to micro level. |
| **`ENDO`** | `int64` | Flag (0 or 1) | No | Endorheic indicator flag: 1 = basin drains to an inland sink/lake with no outlet to the ocean, 0 = exorheic. | 1 indicates closed inland basins (e.g., Sambhar Lake basin in Rajasthan, Ladakh sinks). |
| **`COAST`** | `int64` | Flag (0 or 1) | No | Coastal basin indicator flag: 1 = basin directly touches the coastline, 0 = inland basin. | Filter COAST = 1 to analyze coastal estuaries, backwaters, and sea-level rise vulnerability. |
| **`ORDER`** | `int64` | Integer Rank | No | Hydrological stream ordering of the main drainage reach within the basin. | Higher numbers represent higher order channels. |
| **`SORT`** | `int64` | Integer | No | Topological sorting sequence ensuring downstream basins have higher sort values. | Sort ascending by SORT to process basins in upstream-to-downstream order. |

### Table: `hydrobasins_asia_level_12`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_12. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_12. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYBAS_ID`** | `int64` | Identifier | No | Unique HydroBASINS polygon feature identifier (Pfafstetter hierarchical ID). | Use as primary key for topological basin joins and hierarchical tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`NEXT_SINK`** | `int64` | Identifier | No | HYBAS_ID of the final coastal sink or endorheic inland terminal basin. | Group by NEXT_SINK to identify all basins contributing to a common river mouth or delta. |
| **`MAIN_BAS`** | `int64` | Identifier | No | HYBAS_ID of the overall primary river basin system (e.g., Ganga, Indus, Godavari). | Filter by MAIN_BAS to isolate all sub-basins belonging to a major national river basin. |
| **`DIST_SINK`** | `float64` | Kilometers (km) | No | Distance along the flow path from the basin outlet to the final coastal or terminal sink. | Use for flow travel time and routing delay estimations. |
| **`DIST_MAIN`** | `float64` | Kilometers (km) | No | Distance along the mainstem river channel from the basin outlet to the ocean sink. | Use for river network longitudinal distance calculations. |
| **`SUB_AREA`** | `float64` | Square Kilometers (km²) | ⭐ Yes | Local surface area of this individual sub-basin polygon. | Sum local SUB_AREA or calculate local precipitation volume = SUB_AREA * rainfall. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroBASINS Level 12 (Microwatersheds)). |
| **`UP_AREA`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream drainage area contributing flow through this basin outlet. | UP_AREA > 10,000 indicates major river mainstems; use to distinguish headwaters from main channels. |
| **`PFAF_ID`** | `int64` | Pfafstetter Code | No | Topological Pfafstetter drainage code encoding stream hierarchy and basin topology. | Digits from left to right represent nested basin hierarchy from continental level to micro level. |
| **`ENDO`** | `int64` | Flag (0 or 1) | No | Endorheic indicator flag: 1 = basin drains to an inland sink/lake with no outlet to the ocean, 0 = exorheic. | 1 indicates closed inland basins (e.g., Sambhar Lake basin in Rajasthan, Ladakh sinks). |
| **`COAST`** | `int64` | Flag (0 or 1) | No | Coastal basin indicator flag: 1 = basin directly touches the coastline, 0 = inland basin. | Filter COAST = 1 to analyze coastal estuaries, backwaters, and sea-level rise vulnerability. |
| **`ORDER`** | `int64` | Integer Rank | No | Hydrological stream ordering of the main drainage reach within the basin. | Higher numbers represent higher order channels. |
| **`SORT`** | `int64` | Integer | No | Topological sorting sequence ensuring downstream basins have higher sort values. | Sort ascending by SORT to process basins in upstream-to-downstream order. |

### Table: `hydrobasins_asia_level_2`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_2. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_2. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYBAS_ID`** | `int64` | Identifier | No | Unique HydroBASINS polygon feature identifier (Pfafstetter hierarchical ID). | Use as primary key for topological basin joins and hierarchical tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`NEXT_SINK`** | `int64` | Identifier | No | HYBAS_ID of the final coastal sink or endorheic inland terminal basin. | Group by NEXT_SINK to identify all basins contributing to a common river mouth or delta. |
| **`MAIN_BAS`** | `int64` | Identifier | No | HYBAS_ID of the overall primary river basin system (e.g., Ganga, Indus, Godavari). | Filter by MAIN_BAS to isolate all sub-basins belonging to a major national river basin. |
| **`DIST_SINK`** | `float64` | Kilometers (km) | No | Distance along the flow path from the basin outlet to the final coastal or terminal sink. | Use for flow travel time and routing delay estimations. |
| **`DIST_MAIN`** | `float64` | Kilometers (km) | No | Distance along the mainstem river channel from the basin outlet to the ocean sink. | Use for river network longitudinal distance calculations. |
| **`SUB_AREA`** | `float64` | Square Kilometers (km²) | ⭐ Yes | Local surface area of this individual sub-basin polygon. | Sum local SUB_AREA or calculate local precipitation volume = SUB_AREA * rainfall. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroBASINS Level 2 (Major Regional Basins)). |
| **`UP_AREA`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream drainage area contributing flow through this basin outlet. | UP_AREA > 10,000 indicates major river mainstems; use to distinguish headwaters from main channels. |
| **`PFAF_ID`** | `int64` | Pfafstetter Code | No | Topological Pfafstetter drainage code encoding stream hierarchy and basin topology. | Digits from left to right represent nested basin hierarchy from continental level to micro level. |
| **`ENDO`** | `int64` | Flag (0 or 1) | No | Endorheic indicator flag: 1 = basin drains to an inland sink/lake with no outlet to the ocean, 0 = exorheic. | 1 indicates closed inland basins (e.g., Sambhar Lake basin in Rajasthan, Ladakh sinks). |
| **`COAST`** | `int64` | Flag (0 or 1) | No | Coastal basin indicator flag: 1 = basin directly touches the coastline, 0 = inland basin. | Filter COAST = 1 to analyze coastal estuaries, backwaters, and sea-level rise vulnerability. |
| **`ORDER`** | `int64` | Integer Rank | No | Hydrological stream ordering of the main drainage reach within the basin. | Higher numbers represent higher order channels. |
| **`SORT`** | `int64` | Integer | No | Topological sorting sequence ensuring downstream basins have higher sort values. | Sort ascending by SORT to process basins in upstream-to-downstream order. |

### Table: `hydrobasins_asia_level_3`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_3. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_3. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYBAS_ID`** | `int64` | Identifier | No | Unique HydroBASINS polygon feature identifier (Pfafstetter hierarchical ID). | Use as primary key for topological basin joins and hierarchical tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`NEXT_SINK`** | `int64` | Identifier | No | HYBAS_ID of the final coastal sink or endorheic inland terminal basin. | Group by NEXT_SINK to identify all basins contributing to a common river mouth or delta. |
| **`MAIN_BAS`** | `int64` | Identifier | No | HYBAS_ID of the overall primary river basin system (e.g., Ganga, Indus, Godavari). | Filter by MAIN_BAS to isolate all sub-basins belonging to a major national river basin. |
| **`DIST_SINK`** | `float64` | Kilometers (km) | No | Distance along the flow path from the basin outlet to the final coastal or terminal sink. | Use for flow travel time and routing delay estimations. |
| **`DIST_MAIN`** | `float64` | Kilometers (km) | No | Distance along the mainstem river channel from the basin outlet to the ocean sink. | Use for river network longitudinal distance calculations. |
| **`SUB_AREA`** | `float64` | Square Kilometers (km²) | ⭐ Yes | Local surface area of this individual sub-basin polygon. | Sum local SUB_AREA or calculate local precipitation volume = SUB_AREA * rainfall. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroBASINS Level 3 (Basin Systems)). |
| **`UP_AREA`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream drainage area contributing flow through this basin outlet. | UP_AREA > 10,000 indicates major river mainstems; use to distinguish headwaters from main channels. |
| **`PFAF_ID`** | `int64` | Pfafstetter Code | No | Topological Pfafstetter drainage code encoding stream hierarchy and basin topology. | Digits from left to right represent nested basin hierarchy from continental level to micro level. |
| **`ENDO`** | `int64` | Flag (0 or 1) | No | Endorheic indicator flag: 1 = basin drains to an inland sink/lake with no outlet to the ocean, 0 = exorheic. | 1 indicates closed inland basins (e.g., Sambhar Lake basin in Rajasthan, Ladakh sinks). |
| **`COAST`** | `int64` | Flag (0 or 1) | No | Coastal basin indicator flag: 1 = basin directly touches the coastline, 0 = inland basin. | Filter COAST = 1 to analyze coastal estuaries, backwaters, and sea-level rise vulnerability. |
| **`ORDER`** | `int64` | Integer Rank | No | Hydrological stream ordering of the main drainage reach within the basin. | Higher numbers represent higher order channels. |
| **`SORT`** | `int64` | Integer | No | Topological sorting sequence ensuring downstream basins have higher sort values. | Sort ascending by SORT to process basins in upstream-to-downstream order. |

### Table: `hydrobasins_asia_level_4`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_4. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_4. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYBAS_ID`** | `int64` | Identifier | No | Unique HydroBASINS polygon feature identifier (Pfafstetter hierarchical ID). | Use as primary key for topological basin joins and hierarchical tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`NEXT_SINK`** | `int64` | Identifier | No | HYBAS_ID of the final coastal sink or endorheic inland terminal basin. | Group by NEXT_SINK to identify all basins contributing to a common river mouth or delta. |
| **`MAIN_BAS`** | `int64` | Identifier | No | HYBAS_ID of the overall primary river basin system (e.g., Ganga, Indus, Godavari). | Filter by MAIN_BAS to isolate all sub-basins belonging to a major national river basin. |
| **`DIST_SINK`** | `float64` | Kilometers (km) | No | Distance along the flow path from the basin outlet to the final coastal or terminal sink. | Use for flow travel time and routing delay estimations. |
| **`DIST_MAIN`** | `float64` | Kilometers (km) | No | Distance along the mainstem river channel from the basin outlet to the ocean sink. | Use for river network longitudinal distance calculations. |
| **`SUB_AREA`** | `float64` | Square Kilometers (km²) | ⭐ Yes | Local surface area of this individual sub-basin polygon. | Sum local SUB_AREA or calculate local precipitation volume = SUB_AREA * rainfall. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroBASINS Level 4 (Sub-basin Systems)). |
| **`UP_AREA`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream drainage area contributing flow through this basin outlet. | UP_AREA > 10,000 indicates major river mainstems; use to distinguish headwaters from main channels. |
| **`PFAF_ID`** | `int64` | Pfafstetter Code | No | Topological Pfafstetter drainage code encoding stream hierarchy and basin topology. | Digits from left to right represent nested basin hierarchy from continental level to micro level. |
| **`ENDO`** | `int64` | Flag (0 or 1) | No | Endorheic indicator flag: 1 = basin drains to an inland sink/lake with no outlet to the ocean, 0 = exorheic. | 1 indicates closed inland basins (e.g., Sambhar Lake basin in Rajasthan, Ladakh sinks). |
| **`COAST`** | `int64` | Flag (0 or 1) | No | Coastal basin indicator flag: 1 = basin directly touches the coastline, 0 = inland basin. | Filter COAST = 1 to analyze coastal estuaries, backwaters, and sea-level rise vulnerability. |
| **`ORDER`** | `int64` | Integer Rank | No | Hydrological stream ordering of the main drainage reach within the basin. | Higher numbers represent higher order channels. |
| **`SORT`** | `int64` | Integer | No | Topological sorting sequence ensuring downstream basins have higher sort values. | Sort ascending by SORT to process basins in upstream-to-downstream order. |

### Table: `hydrobasins_asia_level_5`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_5. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_5. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYBAS_ID`** | `int64` | Identifier | No | Unique HydroBASINS polygon feature identifier (Pfafstetter hierarchical ID). | Use as primary key for topological basin joins and hierarchical tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`NEXT_SINK`** | `int64` | Identifier | No | HYBAS_ID of the final coastal sink or endorheic inland terminal basin. | Group by NEXT_SINK to identify all basins contributing to a common river mouth or delta. |
| **`MAIN_BAS`** | `int64` | Identifier | No | HYBAS_ID of the overall primary river basin system (e.g., Ganga, Indus, Godavari). | Filter by MAIN_BAS to isolate all sub-basins belonging to a major national river basin. |
| **`DIST_SINK`** | `float64` | Kilometers (km) | No | Distance along the flow path from the basin outlet to the final coastal or terminal sink. | Use for flow travel time and routing delay estimations. |
| **`DIST_MAIN`** | `float64` | Kilometers (km) | No | Distance along the mainstem river channel from the basin outlet to the ocean sink. | Use for river network longitudinal distance calculations. |
| **`SUB_AREA`** | `float64` | Square Kilometers (km²) | ⭐ Yes | Local surface area of this individual sub-basin polygon. | Sum local SUB_AREA or calculate local precipitation volume = SUB_AREA * rainfall. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroBASINS Level 5 (Watersheds)). |
| **`UP_AREA`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream drainage area contributing flow through this basin outlet. | UP_AREA > 10,000 indicates major river mainstems; use to distinguish headwaters from main channels. |
| **`PFAF_ID`** | `int64` | Pfafstetter Code | No | Topological Pfafstetter drainage code encoding stream hierarchy and basin topology. | Digits from left to right represent nested basin hierarchy from continental level to micro level. |
| **`ENDO`** | `int64` | Flag (0 or 1) | No | Endorheic indicator flag: 1 = basin drains to an inland sink/lake with no outlet to the ocean, 0 = exorheic. | 1 indicates closed inland basins (e.g., Sambhar Lake basin in Rajasthan, Ladakh sinks). |
| **`COAST`** | `int64` | Flag (0 or 1) | No | Coastal basin indicator flag: 1 = basin directly touches the coastline, 0 = inland basin. | Filter COAST = 1 to analyze coastal estuaries, backwaters, and sea-level rise vulnerability. |
| **`ORDER`** | `int64` | Integer Rank | No | Hydrological stream ordering of the main drainage reach within the basin. | Higher numbers represent higher order channels. |
| **`SORT`** | `int64` | Integer | No | Topological sorting sequence ensuring downstream basins have higher sort values. | Sort ascending by SORT to process basins in upstream-to-downstream order. |

### Table: `hydrobasins_asia_level_6`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_6. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_6. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYBAS_ID`** | `int64` | Identifier | No | Unique HydroBASINS polygon feature identifier (Pfafstetter hierarchical ID). | Use as primary key for topological basin joins and hierarchical tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`NEXT_SINK`** | `int64` | Identifier | No | HYBAS_ID of the final coastal sink or endorheic inland terminal basin. | Group by NEXT_SINK to identify all basins contributing to a common river mouth or delta. |
| **`MAIN_BAS`** | `int64` | Identifier | No | HYBAS_ID of the overall primary river basin system (e.g., Ganga, Indus, Godavari). | Filter by MAIN_BAS to isolate all sub-basins belonging to a major national river basin. |
| **`DIST_SINK`** | `float64` | Kilometers (km) | No | Distance along the flow path from the basin outlet to the final coastal or terminal sink. | Use for flow travel time and routing delay estimations. |
| **`DIST_MAIN`** | `float64` | Kilometers (km) | No | Distance along the mainstem river channel from the basin outlet to the ocean sink. | Use for river network longitudinal distance calculations. |
| **`SUB_AREA`** | `float64` | Square Kilometers (km²) | ⭐ Yes | Local surface area of this individual sub-basin polygon. | Sum local SUB_AREA or calculate local precipitation volume = SUB_AREA * rainfall. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroBASINS Level 6 (Sub-watersheds)). |
| **`UP_AREA`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream drainage area contributing flow through this basin outlet. | UP_AREA > 10,000 indicates major river mainstems; use to distinguish headwaters from main channels. |
| **`PFAF_ID`** | `int64` | Pfafstetter Code | No | Topological Pfafstetter drainage code encoding stream hierarchy and basin topology. | Digits from left to right represent nested basin hierarchy from continental level to micro level. |
| **`ENDO`** | `int64` | Flag (0 or 1) | No | Endorheic indicator flag: 1 = basin drains to an inland sink/lake with no outlet to the ocean, 0 = exorheic. | 1 indicates closed inland basins (e.g., Sambhar Lake basin in Rajasthan, Ladakh sinks). |
| **`COAST`** | `int64` | Flag (0 or 1) | No | Coastal basin indicator flag: 1 = basin directly touches the coastline, 0 = inland basin. | Filter COAST = 1 to analyze coastal estuaries, backwaters, and sea-level rise vulnerability. |
| **`ORDER`** | `int64` | Integer Rank | No | Hydrological stream ordering of the main drainage reach within the basin. | Higher numbers represent higher order channels. |
| **`SORT`** | `int64` | Integer | No | Topological sorting sequence ensuring downstream basins have higher sort values. | Sort ascending by SORT to process basins in upstream-to-downstream order. |

### Table: `hydrobasins_asia_level_7`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_7. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_7. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYBAS_ID`** | `int64` | Identifier | No | Unique HydroBASINS polygon feature identifier (Pfafstetter hierarchical ID). | Use as primary key for topological basin joins and hierarchical tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`NEXT_SINK`** | `int64` | Identifier | No | HYBAS_ID of the final coastal sink or endorheic inland terminal basin. | Group by NEXT_SINK to identify all basins contributing to a common river mouth or delta. |
| **`MAIN_BAS`** | `int64` | Identifier | No | HYBAS_ID of the overall primary river basin system (e.g., Ganga, Indus, Godavari). | Filter by MAIN_BAS to isolate all sub-basins belonging to a major national river basin. |
| **`DIST_SINK`** | `float64` | Kilometers (km) | No | Distance along the flow path from the basin outlet to the final coastal or terminal sink. | Use for flow travel time and routing delay estimations. |
| **`DIST_MAIN`** | `float64` | Kilometers (km) | No | Distance along the mainstem river channel from the basin outlet to the ocean sink. | Use for river network longitudinal distance calculations. |
| **`SUB_AREA`** | `float64` | Square Kilometers (km²) | ⭐ Yes | Local surface area of this individual sub-basin polygon. | Sum local SUB_AREA or calculate local precipitation volume = SUB_AREA * rainfall. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroBASINS Level 7 (Drainage Catchments)). |
| **`UP_AREA`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream drainage area contributing flow through this basin outlet. | UP_AREA > 10,000 indicates major river mainstems; use to distinguish headwaters from main channels. |
| **`PFAF_ID`** | `int64` | Pfafstetter Code | No | Topological Pfafstetter drainage code encoding stream hierarchy and basin topology. | Digits from left to right represent nested basin hierarchy from continental level to micro level. |
| **`ENDO`** | `int64` | Flag (0 or 1) | No | Endorheic indicator flag: 1 = basin drains to an inland sink/lake with no outlet to the ocean, 0 = exorheic. | 1 indicates closed inland basins (e.g., Sambhar Lake basin in Rajasthan, Ladakh sinks). |
| **`COAST`** | `int64` | Flag (0 or 1) | No | Coastal basin indicator flag: 1 = basin directly touches the coastline, 0 = inland basin. | Filter COAST = 1 to analyze coastal estuaries, backwaters, and sea-level rise vulnerability. |
| **`ORDER`** | `int64` | Integer Rank | No | Hydrological stream ordering of the main drainage reach within the basin. | Higher numbers represent higher order channels. |
| **`SORT`** | `int64` | Integer | No | Topological sorting sequence ensuring downstream basins have higher sort values. | Sort ascending by SORT to process basins in upstream-to-downstream order. |

### Table: `hydrobasins_asia_level_8`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_8. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_8. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYBAS_ID`** | `int64` | Identifier | No | Unique HydroBASINS polygon feature identifier (Pfafstetter hierarchical ID). | Use as primary key for topological basin joins and hierarchical tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`NEXT_SINK`** | `int64` | Identifier | No | HYBAS_ID of the final coastal sink or endorheic inland terminal basin. | Group by NEXT_SINK to identify all basins contributing to a common river mouth or delta. |
| **`MAIN_BAS`** | `int64` | Identifier | No | HYBAS_ID of the overall primary river basin system (e.g., Ganga, Indus, Godavari). | Filter by MAIN_BAS to isolate all sub-basins belonging to a major national river basin. |
| **`DIST_SINK`** | `float64` | Kilometers (km) | No | Distance along the flow path from the basin outlet to the final coastal or terminal sink. | Use for flow travel time and routing delay estimations. |
| **`DIST_MAIN`** | `float64` | Kilometers (km) | No | Distance along the mainstem river channel from the basin outlet to the ocean sink. | Use for river network longitudinal distance calculations. |
| **`SUB_AREA`** | `float64` | Square Kilometers (km²) | ⭐ Yes | Local surface area of this individual sub-basin polygon. | Sum local SUB_AREA or calculate local precipitation volume = SUB_AREA * rainfall. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroBASINS Level 8 (Catchments)). |
| **`UP_AREA`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream drainage area contributing flow through this basin outlet. | UP_AREA > 10,000 indicates major river mainstems; use to distinguish headwaters from main channels. |
| **`PFAF_ID`** | `int64` | Pfafstetter Code | No | Topological Pfafstetter drainage code encoding stream hierarchy and basin topology. | Digits from left to right represent nested basin hierarchy from continental level to micro level. |
| **`ENDO`** | `int64` | Flag (0 or 1) | No | Endorheic indicator flag: 1 = basin drains to an inland sink/lake with no outlet to the ocean, 0 = exorheic. | 1 indicates closed inland basins (e.g., Sambhar Lake basin in Rajasthan, Ladakh sinks). |
| **`COAST`** | `int64` | Flag (0 or 1) | No | Coastal basin indicator flag: 1 = basin directly touches the coastline, 0 = inland basin. | Filter COAST = 1 to analyze coastal estuaries, backwaters, and sea-level rise vulnerability. |
| **`ORDER`** | `int64` | Integer Rank | No | Hydrological stream ordering of the main drainage reach within the basin. | Higher numbers represent higher order channels. |
| **`SORT`** | `int64` | Integer | No | Topological sorting sequence ensuring downstream basins have higher sort values. | Sort ascending by SORT to process basins in upstream-to-downstream order. |

### Table: `hydrobasins_asia_level_9`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_9. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrobasins_asia_level_9. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYBAS_ID`** | `int64` | Identifier | No | Unique HydroBASINS polygon feature identifier (Pfafstetter hierarchical ID). | Use as primary key for topological basin joins and hierarchical tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`NEXT_SINK`** | `int64` | Identifier | No | HYBAS_ID of the final coastal sink or endorheic inland terminal basin. | Group by NEXT_SINK to identify all basins contributing to a common river mouth or delta. |
| **`MAIN_BAS`** | `int64` | Identifier | No | HYBAS_ID of the overall primary river basin system (e.g., Ganga, Indus, Godavari). | Filter by MAIN_BAS to isolate all sub-basins belonging to a major national river basin. |
| **`DIST_SINK`** | `float64` | Kilometers (km) | No | Distance along the flow path from the basin outlet to the final coastal or terminal sink. | Use for flow travel time and routing delay estimations. |
| **`DIST_MAIN`** | `float64` | Kilometers (km) | No | Distance along the mainstem river channel from the basin outlet to the ocean sink. | Use for river network longitudinal distance calculations. |
| **`SUB_AREA`** | `float64` | Square Kilometers (km²) | ⭐ Yes | Local surface area of this individual sub-basin polygon. | Sum local SUB_AREA or calculate local precipitation volume = SUB_AREA * rainfall. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroBASINS Level 9 (Sub-catchments)). |
| **`UP_AREA`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream drainage area contributing flow through this basin outlet. | UP_AREA > 10,000 indicates major river mainstems; use to distinguish headwaters from main channels. |
| **`PFAF_ID`** | `int64` | Pfafstetter Code | No | Topological Pfafstetter drainage code encoding stream hierarchy and basin topology. | Digits from left to right represent nested basin hierarchy from continental level to micro level. |
| **`ENDO`** | `int64` | Flag (0 or 1) | No | Endorheic indicator flag: 1 = basin drains to an inland sink/lake with no outlet to the ocean, 0 = exorheic. | 1 indicates closed inland basins (e.g., Sambhar Lake basin in Rajasthan, Ladakh sinks). |
| **`COAST`** | `int64` | Flag (0 or 1) | No | Coastal basin indicator flag: 1 = basin directly touches the coastline, 0 = inland basin. | Filter COAST = 1 to analyze coastal estuaries, backwaters, and sea-level rise vulnerability. |
| **`ORDER`** | `int64` | Integer Rank | No | Hydrological stream ordering of the main drainage reach within the basin. | Higher numbers represent higher order channels. |
| **`SORT`** | `int64` | Integer | No | Topological sorting sequence ensuring downstream basins have higher sort values. | Sort ascending by SORT to process basins in upstream-to-downstream order. |

### Table: `hydrolakes_asia_india`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrolakes_asia_india. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrolakes_asia_india. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`Hylak_id`** | `int64` | Identifier | No | Unique HydroLAKES lake/reservoir feature identifier. | Primary key for water bodies. |
| **`Lake_name`** | `str` | Text | No | Official geographic name of the lake, reservoir, or wetland. | Look up named water bodies (e.g., Chilika, Vembanad, Sardar Sarovar, Gobind Sagar). |
| **`Country`** | `str` | Dimensionless / Text | No | Attribute field 'Country' representing record properties in HydroLAKES Lakes & Reservoirs (All India - 11k). | Inspect 'Country' values for querying and filtering features in HydroLAKES Lakes & Reservoirs (All India - 11k). |
| **`Continent`** | `str` | Dimensionless / Text | No | Attribute field 'Continent' representing record properties in HydroLAKES Lakes & Reservoirs (All India - 11k). | Inspect 'Continent' values for querying and filtering features in HydroLAKES Lakes & Reservoirs (All India - 11k). |
| **`Poly_src`** | `str` | Dimensionless / Text | No | Attribute field 'Poly_src' representing record properties in HydroLAKES Lakes & Reservoirs (All India - 11k). | Inspect 'Poly_src' values for querying and filtering features in HydroLAKES Lakes & Reservoirs (All India - 11k). |
| **`Lake_type`** | `int64` | Categorical (1, 2, 3) | ⭐ Yes | Water body typology: 1 = Natural Lake, 2 = Man-made Reservoir, 3 = Regulated Natural Lake. | 1: Natural Lake (turquoise cyan), 2: Man-made Reservoir (royal blue), 3: Regulated Lake with Dam (cobalt blue). (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroLAKES Lakes & Reservoirs (All India - 11k)). |
| **`Grand_id`** | `int64` | Dimensionless / Text | No | Attribute field 'Grand_id' representing record properties in HydroLAKES Lakes & Reservoirs (All India - 11k). | Inspect 'Grand_id' values for querying and filtering features in HydroLAKES Lakes & Reservoirs (All India - 11k). |
| **`Lake_area`** | `float64` | Square Kilometers (km²) | No | Total surface water area of the lake or reservoir polygon. | Multiply by depth to estimate volume; filter Lake_area > 10 for major storage reservoirs. |
| **`Shore_len`** | `float64` | Dimensionless / Text | No | Attribute field 'Shore_len' representing record properties in HydroLAKES Lakes & Reservoirs (All India - 11k). | Inspect 'Shore_len' values for querying and filtering features in HydroLAKES Lakes & Reservoirs (All India - 11k). |
| **`Shore_dev`** | `float64` | Dimensionless / Text | No | Attribute field 'Shore_dev' representing record properties in HydroLAKES Lakes & Reservoirs (All India - 11k). | Inspect 'Shore_dev' values for querying and filtering features in HydroLAKES Lakes & Reservoirs (All India - 11k). |
| **`Vol_total`** | `float64` | Million Cubic Meters (MCM) | No | Estimated total water storage volume capacity. | Total water holding capacity at normal full reservoir level. |
| **`Vol_res`** | `float64` | Million Cubic Meters (MCM) | No | Live/usable reservoir storage volume capacity. | Useful storage capacity for irrigation and municipal water supply. |
| **`Vol_src`** | `int64` | Dimensionless / Text | No | Attribute field 'Vol_src' representing record properties in HydroLAKES Lakes & Reservoirs (All India - 11k). | Inspect 'Vol_src' values for querying and filtering features in HydroLAKES Lakes & Reservoirs (All India - 11k). |
| **`Depth_avg`** | `float64` | Meters (m) | No | Average estimated water depth across the water body surface. | Mean bathymetric depth. |
| **`Dis_avg`** | `float64` | Cubic Meters per Second (m³/s) | No | Average annual outflow discharge through the lake outlet. | Mean outflow rate. |
| **`Res_time`** | `float64` | Dimensionless / Text | No | Attribute field 'Res_time' representing record properties in HydroLAKES Lakes & Reservoirs (All India - 11k). | Inspect 'Res_time' values for querying and filtering features in HydroLAKES Lakes & Reservoirs (All India - 11k). |
| **`Elevation`** | `int64` | Meters above sea level (m) | No | Surface elevation of the lake water surface above mean sea level. | Hydraulic head and altitude. |
| **`Slope_100`** | `float64` | Dimensionless / Text | No | Attribute field 'Slope_100' representing record properties in HydroLAKES Lakes & Reservoirs (All India - 11k). | Inspect 'Slope_100' values for querying and filtering features in HydroLAKES Lakes & Reservoirs (All India - 11k). |
| **`Wshd_area`** | `float64` | Square Kilometers (km²) | No | Total watershed drainage area contributing runoff into the lake. | Ratio Wshd_area / Lake_area indicates lake flushing rate and sedimentation vulnerability. |
| **`Pour_long`** | `float64` | Dimensionless / Text | No | Attribute field 'Pour_long' representing record properties in HydroLAKES Lakes & Reservoirs (All India - 11k). | Inspect 'Pour_long' values for querying and filtering features in HydroLAKES Lakes & Reservoirs (All India - 11k). |
| **`Pour_lat`** | `float64` | Dimensionless / Text | No | Attribute field 'Pour_lat' representing record properties in HydroLAKES Lakes & Reservoirs (All India - 11k). | Inspect 'Pour_lat' values for querying and filtering features in HydroLAKES Lakes & Reservoirs (All India - 11k). |

### Table: `hydrorivers_asia_india`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_asia_india. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_asia_india. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYRIV_ID`** | `int64` | Identifier | No | Unique HydroRIVERS line feature identifier for each individual river reach. | Primary key for stream reaches and network tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`MAIN_RIV`** | `int64` | Identifier | No | HYRIV_ID of the major trunk river reach representing the primary river outlet. | Group by MAIN_RIV to isolate complete river networks. |
| **`LENGTH_KM`** | `float64` | Kilometers (km) | No | Physical channel reach length along the streamline. | Multiply by flow velocity to estimate reach travel time; sum for river system length. |
| **`DIST_DN_KM`** | `float64` | Kilometers (km) | No | Total river network distance from the reach downstream endpoint to the ocean/sink. | Longitudinal distance to outlet. |
| **`DIST_UP_KM`** | `float64` | Kilometers (km) | No | Total distance from the reach upstream endpoint to the farthest headwater source. | River length from source. |
| **`CATCH_SKM`** | `float64` | Square Kilometers (km²) | No | Direct local catchment area draining into this specific river reach. | Local reach catchment runoff area. |
| **`UPLAND_SKM`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream watershed area contributing to this reach. | Key hydrologic scale parameter: defines total drainage basin area at this point in the river. |
| **`ENDORHEIC`** | `int64` | Flag (0 or 1) | No | Flag indicating reach is part of an endorheic (inland drainage) system. | 1 = reach does not drain to the sea. |
| **`DIS_AV_CMS`** | `float64` | Cubic Meters per Second (m³/s) | No | Long-term annual average natural river discharge (mean annual flow rate). | Core flow volume metric: DIS_AV_CMS > 500 represents major navigable rivers; < 5 represents minor creeks. |
| **`ORD_STRA`** | `int64` | Integer (1-8) | ⭐ Yes | Strahler Stream Order (1 = headwater stream, 8 = mega-trunk estuary). | 1: Headwaters (134k reaches), 2: Secondary (59k), 3: Tertiary (32k), 4: Sub-Rivers (18k), 5: Medium Rivers (9.5k), 6: Major Rivers (4.5k), 7: Trunk Rivers (1.5k), 8: Estuaries (1.2k). (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroRIVERS Stream Network (All India - 261k Reaches)). |
| **`ORD_CLAS`** | `int64` | Integer (1-4) | No | Cartographic classification rank based on discharge volume for zoom-dependent rendering. | 1 = major continental river, 4 = minor local stream. |
| **`ORD_FLOW`** | `int64` | Integer (1-7) | No | Flow volume order hierarchy indicating river magnitude. | Use for flow-based filtering and graduated line thickness. |
| **`HYBAS_L12`** | `int64` | Dimensionless / Text | No | Attribute field 'HYBAS_L12' representing record properties in HydroRIVERS Stream Network (All India - 261k Reaches). | Inspect 'HYBAS_L12' values for querying and filtering features in HydroRIVERS Stream Network (All India - 261k Reaches). |

### Table: `hydrorivers_india_order_1`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_1. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_1. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYRIV_ID`** | `int64` | Identifier | No | Unique HydroRIVERS line feature identifier for each individual river reach. | Primary key for stream reaches and network tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`MAIN_RIV`** | `int64` | Identifier | No | HYRIV_ID of the major trunk river reach representing the primary river outlet. | Group by MAIN_RIV to isolate complete river networks. |
| **`LENGTH_KM`** | `float64` | Kilometers (km) | No | Physical channel reach length along the streamline. | Multiply by flow velocity to estimate reach travel time; sum for river system length. |
| **`DIST_DN_KM`** | `float64` | Kilometers (km) | No | Total river network distance from the reach downstream endpoint to the ocean/sink. | Longitudinal distance to outlet. |
| **`DIST_UP_KM`** | `float64` | Kilometers (km) | No | Total distance from the reach upstream endpoint to the farthest headwater source. | River length from source. |
| **`CATCH_SKM`** | `float64` | Square Kilometers (km²) | No | Direct local catchment area draining into this specific river reach. | Local reach catchment runoff area. |
| **`UPLAND_SKM`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream watershed area contributing to this reach. | Key hydrologic scale parameter: defines total drainage basin area at this point in the river. |
| **`ENDORHEIC`** | `int64` | Flag (0 or 1) | No | Flag indicating reach is part of an endorheic (inland drainage) system. | 1 = reach does not drain to the sea. |
| **`DIS_AV_CMS`** | `float64` | Cubic Meters per Second (m³/s) | No | Long-term annual average natural river discharge (mean annual flow rate). | Core flow volume metric: DIS_AV_CMS > 500 represents major navigable rivers; < 5 represents minor creeks. |
| **`ORD_STRA`** | `int64` | Integer (1-8) | ⭐ Yes | Strahler Stream Order (1 = headwater stream, 8 = mega-trunk estuary). | 1: Headwaters (134k reaches), 2: Secondary (59k), 3: Tertiary (32k), 4: Sub-Rivers (18k), 5: Medium Rivers (9.5k), 6: Major Rivers (4.5k), 7: Trunk Rivers (1.5k), 8: Estuaries (1.2k). (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroRIVERS Order 1 (Headwater Streams)). |
| **`ORD_CLAS`** | `int64` | Integer (1-4) | No | Cartographic classification rank based on discharge volume for zoom-dependent rendering. | 1 = major continental river, 4 = minor local stream. |
| **`ORD_FLOW`** | `int64` | Integer (1-7) | No | Flow volume order hierarchy indicating river magnitude. | Use for flow-based filtering and graduated line thickness. |
| **`HYBAS_L12`** | `int64` | Dimensionless / Text | No | Attribute field 'HYBAS_L12' representing record properties in HydroRIVERS Order 1 (Headwater Streams). | Inspect 'HYBAS_L12' values for querying and filtering features in HydroRIVERS Order 1 (Headwater Streams). |

### Table: `hydrorivers_india_order_2`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_2. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_2. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYRIV_ID`** | `int64` | Identifier | No | Unique HydroRIVERS line feature identifier for each individual river reach. | Primary key for stream reaches and network tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`MAIN_RIV`** | `int64` | Identifier | No | HYRIV_ID of the major trunk river reach representing the primary river outlet. | Group by MAIN_RIV to isolate complete river networks. |
| **`LENGTH_KM`** | `float64` | Kilometers (km) | No | Physical channel reach length along the streamline. | Multiply by flow velocity to estimate reach travel time; sum for river system length. |
| **`DIST_DN_KM`** | `float64` | Kilometers (km) | No | Total river network distance from the reach downstream endpoint to the ocean/sink. | Longitudinal distance to outlet. |
| **`DIST_UP_KM`** | `float64` | Kilometers (km) | No | Total distance from the reach upstream endpoint to the farthest headwater source. | River length from source. |
| **`CATCH_SKM`** | `float64` | Square Kilometers (km²) | No | Direct local catchment area draining into this specific river reach. | Local reach catchment runoff area. |
| **`UPLAND_SKM`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream watershed area contributing to this reach. | Key hydrologic scale parameter: defines total drainage basin area at this point in the river. |
| **`ENDORHEIC`** | `int64` | Flag (0 or 1) | No | Flag indicating reach is part of an endorheic (inland drainage) system. | 1 = reach does not drain to the sea. |
| **`DIS_AV_CMS`** | `float64` | Cubic Meters per Second (m³/s) | No | Long-term annual average natural river discharge (mean annual flow rate). | Core flow volume metric: DIS_AV_CMS > 500 represents major navigable rivers; < 5 represents minor creeks. |
| **`ORD_STRA`** | `int64` | Integer (1-8) | ⭐ Yes | Strahler Stream Order (1 = headwater stream, 8 = mega-trunk estuary). | 1: Headwaters (134k reaches), 2: Secondary (59k), 3: Tertiary (32k), 4: Sub-Rivers (18k), 5: Medium Rivers (9.5k), 6: Major Rivers (4.5k), 7: Trunk Rivers (1.5k), 8: Estuaries (1.2k). (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroRIVERS Order 2 (Secondary Streams)). |
| **`ORD_CLAS`** | `int64` | Integer (1-4) | No | Cartographic classification rank based on discharge volume for zoom-dependent rendering. | 1 = major continental river, 4 = minor local stream. |
| **`ORD_FLOW`** | `int64` | Integer (1-7) | No | Flow volume order hierarchy indicating river magnitude. | Use for flow-based filtering and graduated line thickness. |
| **`HYBAS_L12`** | `int64` | Dimensionless / Text | No | Attribute field 'HYBAS_L12' representing record properties in HydroRIVERS Order 2 (Secondary Streams). | Inspect 'HYBAS_L12' values for querying and filtering features in HydroRIVERS Order 2 (Secondary Streams). |

### Table: `hydrorivers_india_order_3`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_3. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_3. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYRIV_ID`** | `int64` | Identifier | No | Unique HydroRIVERS line feature identifier for each individual river reach. | Primary key for stream reaches and network tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`MAIN_RIV`** | `int64` | Identifier | No | HYRIV_ID of the major trunk river reach representing the primary river outlet. | Group by MAIN_RIV to isolate complete river networks. |
| **`LENGTH_KM`** | `float64` | Kilometers (km) | No | Physical channel reach length along the streamline. | Multiply by flow velocity to estimate reach travel time; sum for river system length. |
| **`DIST_DN_KM`** | `float64` | Kilometers (km) | No | Total river network distance from the reach downstream endpoint to the ocean/sink. | Longitudinal distance to outlet. |
| **`DIST_UP_KM`** | `float64` | Kilometers (km) | No | Total distance from the reach upstream endpoint to the farthest headwater source. | River length from source. |
| **`CATCH_SKM`** | `float64` | Square Kilometers (km²) | No | Direct local catchment area draining into this specific river reach. | Local reach catchment runoff area. |
| **`UPLAND_SKM`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream watershed area contributing to this reach. | Key hydrologic scale parameter: defines total drainage basin area at this point in the river. |
| **`ENDORHEIC`** | `int64` | Flag (0 or 1) | No | Flag indicating reach is part of an endorheic (inland drainage) system. | 1 = reach does not drain to the sea. |
| **`DIS_AV_CMS`** | `float64` | Cubic Meters per Second (m³/s) | No | Long-term annual average natural river discharge (mean annual flow rate). | Core flow volume metric: DIS_AV_CMS > 500 represents major navigable rivers; < 5 represents minor creeks. |
| **`ORD_STRA`** | `int64` | Integer (1-8) | ⭐ Yes | Strahler Stream Order (1 = headwater stream, 8 = mega-trunk estuary). | 1: Headwaters (134k reaches), 2: Secondary (59k), 3: Tertiary (32k), 4: Sub-Rivers (18k), 5: Medium Rivers (9.5k), 6: Major Rivers (4.5k), 7: Trunk Rivers (1.5k), 8: Estuaries (1.2k). (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroRIVERS Order 3 (Tertiary Streams)). |
| **`ORD_CLAS`** | `int64` | Integer (1-4) | No | Cartographic classification rank based on discharge volume for zoom-dependent rendering. | 1 = major continental river, 4 = minor local stream. |
| **`ORD_FLOW`** | `int64` | Integer (1-7) | No | Flow volume order hierarchy indicating river magnitude. | Use for flow-based filtering and graduated line thickness. |
| **`HYBAS_L12`** | `int64` | Dimensionless / Text | No | Attribute field 'HYBAS_L12' representing record properties in HydroRIVERS Order 3 (Tertiary Streams). | Inspect 'HYBAS_L12' values for querying and filtering features in HydroRIVERS Order 3 (Tertiary Streams). |

### Table: `hydrorivers_india_order_4`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_4. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_4. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYRIV_ID`** | `int64` | Identifier | No | Unique HydroRIVERS line feature identifier for each individual river reach. | Primary key for stream reaches and network tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`MAIN_RIV`** | `int64` | Identifier | No | HYRIV_ID of the major trunk river reach representing the primary river outlet. | Group by MAIN_RIV to isolate complete river networks. |
| **`LENGTH_KM`** | `float64` | Kilometers (km) | No | Physical channel reach length along the streamline. | Multiply by flow velocity to estimate reach travel time; sum for river system length. |
| **`DIST_DN_KM`** | `float64` | Kilometers (km) | No | Total river network distance from the reach downstream endpoint to the ocean/sink. | Longitudinal distance to outlet. |
| **`DIST_UP_KM`** | `float64` | Kilometers (km) | No | Total distance from the reach upstream endpoint to the farthest headwater source. | River length from source. |
| **`CATCH_SKM`** | `float64` | Square Kilometers (km²) | No | Direct local catchment area draining into this specific river reach. | Local reach catchment runoff area. |
| **`UPLAND_SKM`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream watershed area contributing to this reach. | Key hydrologic scale parameter: defines total drainage basin area at this point in the river. |
| **`ENDORHEIC`** | `int64` | Flag (0 or 1) | No | Flag indicating reach is part of an endorheic (inland drainage) system. | 1 = reach does not drain to the sea. |
| **`DIS_AV_CMS`** | `float64` | Cubic Meters per Second (m³/s) | No | Long-term annual average natural river discharge (mean annual flow rate). | Core flow volume metric: DIS_AV_CMS > 500 represents major navigable rivers; < 5 represents minor creeks. |
| **`ORD_STRA`** | `int64` | Integer (1-8) | ⭐ Yes | Strahler Stream Order (1 = headwater stream, 8 = mega-trunk estuary). | 1: Headwaters (134k reaches), 2: Secondary (59k), 3: Tertiary (32k), 4: Sub-Rivers (18k), 5: Medium Rivers (9.5k), 6: Major Rivers (4.5k), 7: Trunk Rivers (1.5k), 8: Estuaries (1.2k). (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroRIVERS Order 4 (Sub-Rivers)). |
| **`ORD_CLAS`** | `int64` | Integer (1-4) | No | Cartographic classification rank based on discharge volume for zoom-dependent rendering. | 1 = major continental river, 4 = minor local stream. |
| **`ORD_FLOW`** | `int64` | Integer (1-7) | No | Flow volume order hierarchy indicating river magnitude. | Use for flow-based filtering and graduated line thickness. |
| **`HYBAS_L12`** | `int64` | Dimensionless / Text | No | Attribute field 'HYBAS_L12' representing record properties in HydroRIVERS Order 4 (Sub-Rivers). | Inspect 'HYBAS_L12' values for querying and filtering features in HydroRIVERS Order 4 (Sub-Rivers). |

### Table: `hydrorivers_india_order_5`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_5. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_5. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYRIV_ID`** | `int64` | Identifier | No | Unique HydroRIVERS line feature identifier for each individual river reach. | Primary key for stream reaches and network tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`MAIN_RIV`** | `int64` | Identifier | No | HYRIV_ID of the major trunk river reach representing the primary river outlet. | Group by MAIN_RIV to isolate complete river networks. |
| **`LENGTH_KM`** | `float64` | Kilometers (km) | No | Physical channel reach length along the streamline. | Multiply by flow velocity to estimate reach travel time; sum for river system length. |
| **`DIST_DN_KM`** | `float64` | Kilometers (km) | No | Total river network distance from the reach downstream endpoint to the ocean/sink. | Longitudinal distance to outlet. |
| **`DIST_UP_KM`** | `float64` | Kilometers (km) | No | Total distance from the reach upstream endpoint to the farthest headwater source. | River length from source. |
| **`CATCH_SKM`** | `float64` | Square Kilometers (km²) | No | Direct local catchment area draining into this specific river reach. | Local reach catchment runoff area. |
| **`UPLAND_SKM`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream watershed area contributing to this reach. | Key hydrologic scale parameter: defines total drainage basin area at this point in the river. |
| **`ENDORHEIC`** | `int64` | Flag (0 or 1) | No | Flag indicating reach is part of an endorheic (inland drainage) system. | 1 = reach does not drain to the sea. |
| **`DIS_AV_CMS`** | `float64` | Cubic Meters per Second (m³/s) | No | Long-term annual average natural river discharge (mean annual flow rate). | Core flow volume metric: DIS_AV_CMS > 500 represents major navigable rivers; < 5 represents minor creeks. |
| **`ORD_STRA`** | `int64` | Integer (1-8) | ⭐ Yes | Strahler Stream Order (1 = headwater stream, 8 = mega-trunk estuary). | 1: Headwaters (134k reaches), 2: Secondary (59k), 3: Tertiary (32k), 4: Sub-Rivers (18k), 5: Medium Rivers (9.5k), 6: Major Rivers (4.5k), 7: Trunk Rivers (1.5k), 8: Estuaries (1.2k). (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroRIVERS Order 5 (Medium Rivers)). |
| **`ORD_CLAS`** | `int64` | Integer (1-4) | No | Cartographic classification rank based on discharge volume for zoom-dependent rendering. | 1 = major continental river, 4 = minor local stream. |
| **`ORD_FLOW`** | `int64` | Integer (1-7) | No | Flow volume order hierarchy indicating river magnitude. | Use for flow-based filtering and graduated line thickness. |
| **`HYBAS_L12`** | `int64` | Dimensionless / Text | No | Attribute field 'HYBAS_L12' representing record properties in HydroRIVERS Order 5 (Medium Rivers). | Inspect 'HYBAS_L12' values for querying and filtering features in HydroRIVERS Order 5 (Medium Rivers). |

### Table: `hydrorivers_india_order_6`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_6. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_6. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYRIV_ID`** | `int64` | Identifier | No | Unique HydroRIVERS line feature identifier for each individual river reach. | Primary key for stream reaches and network tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`MAIN_RIV`** | `int64` | Identifier | No | HYRIV_ID of the major trunk river reach representing the primary river outlet. | Group by MAIN_RIV to isolate complete river networks. |
| **`LENGTH_KM`** | `float64` | Kilometers (km) | No | Physical channel reach length along the streamline. | Multiply by flow velocity to estimate reach travel time; sum for river system length. |
| **`DIST_DN_KM`** | `float64` | Kilometers (km) | No | Total river network distance from the reach downstream endpoint to the ocean/sink. | Longitudinal distance to outlet. |
| **`DIST_UP_KM`** | `float64` | Kilometers (km) | No | Total distance from the reach upstream endpoint to the farthest headwater source. | River length from source. |
| **`CATCH_SKM`** | `float64` | Square Kilometers (km²) | No | Direct local catchment area draining into this specific river reach. | Local reach catchment runoff area. |
| **`UPLAND_SKM`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream watershed area contributing to this reach. | Key hydrologic scale parameter: defines total drainage basin area at this point in the river. |
| **`ENDORHEIC`** | `int64` | Flag (0 or 1) | No | Flag indicating reach is part of an endorheic (inland drainage) system. | 1 = reach does not drain to the sea. |
| **`DIS_AV_CMS`** | `float64` | Cubic Meters per Second (m³/s) | No | Long-term annual average natural river discharge (mean annual flow rate). | Core flow volume metric: DIS_AV_CMS > 500 represents major navigable rivers; < 5 represents minor creeks. |
| **`ORD_STRA`** | `int64` | Integer (1-8) | ⭐ Yes | Strahler Stream Order (1 = headwater stream, 8 = mega-trunk estuary). | 1: Headwaters (134k reaches), 2: Secondary (59k), 3: Tertiary (32k), 4: Sub-Rivers (18k), 5: Medium Rivers (9.5k), 6: Major Rivers (4.5k), 7: Trunk Rivers (1.5k), 8: Estuaries (1.2k). (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroRIVERS Order 6 (Major Rivers)). |
| **`ORD_CLAS`** | `int64` | Integer (1-4) | No | Cartographic classification rank based on discharge volume for zoom-dependent rendering. | 1 = major continental river, 4 = minor local stream. |
| **`ORD_FLOW`** | `int64` | Integer (1-7) | No | Flow volume order hierarchy indicating river magnitude. | Use for flow-based filtering and graduated line thickness. |
| **`HYBAS_L12`** | `int64` | Dimensionless / Text | No | Attribute field 'HYBAS_L12' representing record properties in HydroRIVERS Order 6 (Major Rivers). | Inspect 'HYBAS_L12' values for querying and filtering features in HydroRIVERS Order 6 (Major Rivers). |

### Table: `hydrorivers_india_order_7`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_7. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_7. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYRIV_ID`** | `int64` | Identifier | No | Unique HydroRIVERS line feature identifier for each individual river reach. | Primary key for stream reaches and network tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`MAIN_RIV`** | `int64` | Identifier | No | HYRIV_ID of the major trunk river reach representing the primary river outlet. | Group by MAIN_RIV to isolate complete river networks. |
| **`LENGTH_KM`** | `float64` | Kilometers (km) | No | Physical channel reach length along the streamline. | Multiply by flow velocity to estimate reach travel time; sum for river system length. |
| **`DIST_DN_KM`** | `float64` | Kilometers (km) | No | Total river network distance from the reach downstream endpoint to the ocean/sink. | Longitudinal distance to outlet. |
| **`DIST_UP_KM`** | `float64` | Kilometers (km) | No | Total distance from the reach upstream endpoint to the farthest headwater source. | River length from source. |
| **`CATCH_SKM`** | `float64` | Square Kilometers (km²) | No | Direct local catchment area draining into this specific river reach. | Local reach catchment runoff area. |
| **`UPLAND_SKM`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream watershed area contributing to this reach. | Key hydrologic scale parameter: defines total drainage basin area at this point in the river. |
| **`ENDORHEIC`** | `int64` | Flag (0 or 1) | No | Flag indicating reach is part of an endorheic (inland drainage) system. | 1 = reach does not drain to the sea. |
| **`DIS_AV_CMS`** | `float64` | Cubic Meters per Second (m³/s) | No | Long-term annual average natural river discharge (mean annual flow rate). | Core flow volume metric: DIS_AV_CMS > 500 represents major navigable rivers; < 5 represents minor creeks. |
| **`ORD_STRA`** | `int64` | Integer (1-8) | ⭐ Yes | Strahler Stream Order (1 = headwater stream, 8 = mega-trunk estuary). | 1: Headwaters (134k reaches), 2: Secondary (59k), 3: Tertiary (32k), 4: Sub-Rivers (18k), 5: Medium Rivers (9.5k), 6: Major Rivers (4.5k), 7: Trunk Rivers (1.5k), 8: Estuaries (1.2k). (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroRIVERS Order 7 (Large Trunk Rivers)). |
| **`ORD_CLAS`** | `int64` | Integer (1-4) | No | Cartographic classification rank based on discharge volume for zoom-dependent rendering. | 1 = major continental river, 4 = minor local stream. |
| **`ORD_FLOW`** | `int64` | Integer (1-7) | No | Flow volume order hierarchy indicating river magnitude. | Use for flow-based filtering and graduated line thickness. |
| **`HYBAS_L12`** | `int64` | Dimensionless / Text | No | Attribute field 'HYBAS_L12' representing record properties in HydroRIVERS Order 7 (Large Trunk Rivers). | Inspect 'HYBAS_L12' values for querying and filtering features in HydroRIVERS Order 7 (Large Trunk Rivers). |

### Table: `hydrorivers_india_order_8`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_8. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for hydrorivers_india_order_8. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`HYRIV_ID`** | `int64` | Identifier | No | Unique HydroRIVERS line feature identifier for each individual river reach. | Primary key for stream reaches and network tracing. |
| **`NEXT_DOWN`** | `int64` | Identifier | No | HYRIV_ID of the next immediately downstream connected reach. | Traverse NEXT_DOWN iteratively to trace river flows downstream. |
| **`MAIN_RIV`** | `int64` | Identifier | No | HYRIV_ID of the major trunk river reach representing the primary river outlet. | Group by MAIN_RIV to isolate complete river networks. |
| **`LENGTH_KM`** | `float64` | Kilometers (km) | No | Physical channel reach length along the streamline. | Multiply by flow velocity to estimate reach travel time; sum for river system length. |
| **`DIST_DN_KM`** | `float64` | Kilometers (km) | No | Total river network distance from the reach downstream endpoint to the ocean/sink. | Longitudinal distance to outlet. |
| **`DIST_UP_KM`** | `float64` | Kilometers (km) | No | Total distance from the reach upstream endpoint to the farthest headwater source. | River length from source. |
| **`CATCH_SKM`** | `float64` | Square Kilometers (km²) | No | Direct local catchment area draining into this specific river reach. | Local reach catchment runoff area. |
| **`UPLAND_SKM`** | `float64` | Square Kilometers (km²) | No | Total accumulated upstream watershed area contributing to this reach. | Key hydrologic scale parameter: defines total drainage basin area at this point in the river. |
| **`ENDORHEIC`** | `int64` | Flag (0 or 1) | No | Flag indicating reach is part of an endorheic (inland drainage) system. | 1 = reach does not drain to the sea. |
| **`DIS_AV_CMS`** | `float64` | Cubic Meters per Second (m³/s) | No | Long-term annual average natural river discharge (mean annual flow rate). | Core flow volume metric: DIS_AV_CMS > 500 represents major navigable rivers; < 5 represents minor creeks. |
| **`ORD_STRA`** | `int64` | Integer (1-8) | ⭐ Yes | Strahler Stream Order (1 = headwater stream, 8 = mega-trunk estuary). | 1: Headwaters (134k reaches), 2: Secondary (59k), 3: Tertiary (32k), 4: Sub-Rivers (18k), 5: Medium Rivers (9.5k), 6: Major Rivers (4.5k), 7: Trunk Rivers (1.5k), 8: Estuaries (1.2k). (PRIMARY THEMATIC KEY: used for standard cartographic categorization of HydroRIVERS Order 8 (Mega River Estuaries & Outlets)). |
| **`ORD_CLAS`** | `int64` | Integer (1-4) | No | Cartographic classification rank based on discharge volume for zoom-dependent rendering. | 1 = major continental river, 4 = minor local stream. |
| **`ORD_FLOW`** | `int64` | Integer (1-7) | No | Flow volume order hierarchy indicating river magnitude. | Use for flow-based filtering and graduated line thickness. |
| **`HYBAS_L12`** | `int64` | Dimensionless / Text | No | Attribute field 'HYBAS_L12' representing record properties in HydroRIVERS Order 8 (Mega River Estuaries & Outlets). | Inspect 'HYBAS_L12' values for querying and filtering features in HydroRIVERS Order 8 (Mega River Estuaries & Outlets). |

### Table: `india_boundary_indian_boundary`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for india_boundary_indian_boundary. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for india_boundary_indian_boundary. | Use for indexing and exact feature identification; do not use as a physical domain variable. |

### Table: `india_geoportal_data_gis_geopackage_india_geoportal_layers_indi_1`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for india_geoportal_data_gis_geopackage_india_geoportal_layers_indi_1. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for india_geoportal_data_gis_geopackage_india_geoportal_layers_indi_1. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`dissolve`** | `str` | Dimensionless / Text | No | Attribute field 'dissolve' representing record properties in India Major Rivers Network. | Inspect 'dissolve' values for querying and filtering features in India Major Rivers Network. |
| **`scalerank`** | `float64` | Dimensionless / Text | No | Attribute field 'scalerank' representing record properties in India Major Rivers Network. | Inspect 'scalerank' values for querying and filtering features in India Major Rivers Network. |
| **`featurecla`** | `str` | Categorical | No | Natural Earth / Open Portal geographic feature classification. | Admin-0 capital (national capital), Admin-1 capital (state capital), Populated place (major city), River, Port. |
| **`name`** | `str` | Dimensionless / Text | ⭐ Yes | Attribute field 'name' representing record properties in India Major Rivers Network. | Inspect 'name' values for querying and filtering features in India Major Rivers Network. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of India Major Rivers Network). |
| **`name_alt`** | `str` | Dimensionless / Text | No | Attribute field 'name_alt' representing record properties in India Major Rivers Network. | Inspect 'name_alt' values for querying and filtering features in India Major Rivers Network. |
| **`rivernum`** | `int64` | Dimensionless / Text | No | Attribute field 'rivernum' representing record properties in India Major Rivers Network. | Inspect 'rivernum' values for querying and filtering features in India Major Rivers Network. |
| **`note`** | `object` | Dimensionless / Text | No | Attribute field 'note' representing record properties in India Major Rivers Network. | Inspect 'note' values for querying and filtering features in India Major Rivers Network. |
| **`min_zoom`** | `float64` | Dimensionless / Text | No | Attribute field 'min_zoom' representing record properties in India Major Rivers Network. | Inspect 'min_zoom' values for querying and filtering features in India Major Rivers Network. |
| **`name_en`** | `str` | Dimensionless / Text | No | Attribute field 'name_en' representing record properties in India Major Rivers Network. | Inspect 'name_en' values for querying and filtering features in India Major Rivers Network. |
| **`min_label`** | `float64` | Dimensionless / Text | No | Attribute field 'min_label' representing record properties in India Major Rivers Network. | Inspect 'min_label' values for querying and filtering features in India Major Rivers Network. |

### Table: `overture_administrative_divisions`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for overture_administrative_divisions. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for overture_administrative_divisions. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`id`** | `str` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for overture_administrative_divisions. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`country`** | `str` | Dimensionless / Text | No | Attribute field 'country' representing record properties in Overture Administrative Divisions (India). | Inspect 'country' values for querying and filtering features in Overture Administrative Divisions (India). |
| **`sources`** | `str` | Dimensionless / Text | No | Attribute field 'sources' representing record properties in Overture Administrative Divisions (India). | Inspect 'sources' values for querying and filtering features in Overture Administrative Divisions (India). |
| **`subtype`** | `str` | Categorical | ⭐ Yes | Feature structural subtype classification. | Admin: region (state), county (district), locality (tehsil/city), neighborhood. Utility: power, water, bridge, barrier, pedestrian. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of Overture Administrative Divisions (India)). |
| **`admin_level`** | `float64` | Integer (1, 2) | No | Overture administrative level hierarchy rank. | 1 = First-order state/region, 2 = Second-order district/county. |
| **`class`** | `str` | Categorical | No | Detailed functional class tag. | power_line, breakwater, generator, power_tower, toll_booth. |
| **`names`** | `str` | Dimensionless / Text | No | Attribute field 'names' representing record properties in Overture Administrative Divisions (India). | Inspect 'names' values for querying and filtering features in Overture Administrative Divisions (India). |
| **`is_land`** | `int64` | Dimensionless / Text | No | Attribute field 'is_land' representing record properties in Overture Administrative Divisions (India). | Inspect 'is_land' values for querying and filtering features in Overture Administrative Divisions (India). |
| **`is_territorial`** | `int64` | Dimensionless / Text | No | Attribute field 'is_territorial' representing record properties in Overture Administrative Divisions (India). | Inspect 'is_territorial' values for querying and filtering features in Overture Administrative Divisions (India). |
| **`region`** | `str` | Dimensionless / Text | No | Attribute field 'region' representing record properties in Overture Administrative Divisions (India). | Inspect 'region' values for querying and filtering features in Overture Administrative Divisions (India). |
| **`division_id`** | `str` | Dimensionless / Text | No | Attribute field 'division_id' representing record properties in Overture Administrative Divisions (India). | Inspect 'division_id' values for querying and filtering features in Overture Administrative Divisions (India). |
| **`version`** | `int64` | Dimensionless / Text | No | Attribute field 'version' representing record properties in Overture Administrative Divisions (India). | Inspect 'version' values for querying and filtering features in Overture Administrative Divisions (India). |
| **`bbox`** | `str` | Dimensionless / Text | No | Attribute field 'bbox' representing record properties in Overture Administrative Divisions (India). | Inspect 'bbox' values for querying and filtering features in Overture Administrative Divisions (India). |

### Table: `overture_utility_infrastructure`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for overture_utility_infrastructure. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for overture_utility_infrastructure. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`id`** | `str` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for overture_utility_infrastructure. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`sources`** | `str` | Dimensionless / Text | No | Attribute field 'sources' representing record properties in Overture Utility & Power Infrastructure (All India - 2.6M). | Inspect 'sources' values for querying and filtering features in Overture Utility & Power Infrastructure (All India - 2.6M). |
| **`names`** | `object` | Dimensionless / Text | No | Attribute field 'names' representing record properties in Overture Utility & Power Infrastructure (All India - 2.6M). | Inspect 'names' values for querying and filtering features in Overture Utility & Power Infrastructure (All India - 2.6M). |
| **`level`** | `float64` | Dimensionless / Text | No | Attribute field 'level' representing record properties in Overture Utility & Power Infrastructure (All India - 2.6M). | Inspect 'level' values for querying and filtering features in Overture Utility & Power Infrastructure (All India - 2.6M). |
| **`wikidata`** | `object` | Dimensionless / Text | No | Attribute field 'wikidata' representing record properties in Overture Utility & Power Infrastructure (All India - 2.6M). | Inspect 'wikidata' values for querying and filtering features in Overture Utility & Power Infrastructure (All India - 2.6M). |
| **`source_tags`** | `str` | Dimensionless / Text | No | Attribute field 'source_tags' representing record properties in Overture Utility & Power Infrastructure (All India - 2.6M). | Inspect 'source_tags' values for querying and filtering features in Overture Utility & Power Infrastructure (All India - 2.6M). |
| **`subtype`** | `str` | Categorical | ⭐ Yes | Feature structural subtype classification. | Admin: region (state), county (district), locality (tehsil/city), neighborhood. Utility: power, water, bridge, barrier, pedestrian. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of Overture Utility & Power Infrastructure (All India - 2.6M)). |
| **`class`** | `str` | Categorical | No | Detailed functional class tag. | power_line, breakwater, generator, power_tower, toll_booth. |
| **`height`** | `object` | Dimensionless / Text | No | Attribute field 'height' representing record properties in Overture Utility & Power Infrastructure (All India - 2.6M). | Inspect 'height' values for querying and filtering features in Overture Utility & Power Infrastructure (All India - 2.6M). |
| **`surface`** | `object` | Dimensionless / Text | No | Attribute field 'surface' representing record properties in Overture Utility & Power Infrastructure (All India - 2.6M). | Inspect 'surface' values for querying and filtering features in Overture Utility & Power Infrastructure (All India - 2.6M). |
| **`version`** | `int64` | Dimensionless / Text | No | Attribute field 'version' representing record properties in Overture Utility & Power Infrastructure (All India - 2.6M). | Inspect 'version' values for querying and filtering features in Overture Utility & Power Infrastructure (All India - 2.6M). |
| **`bbox`** | `str` | Dimensionless / Text | No | Attribute field 'bbox' representing record properties in Overture Utility & Power Infrastructure (All India - 2.6M). | Inspect 'bbox' values for querying and filtering features in Overture Utility & Power Infrastructure (All India - 2.6M). |

### Table: `parliamentary_constituencies_lok_sabha`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for parliamentary_constituencies_lok_sabha. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for parliamentary_constituencies_lok_sabha. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`pc_id`** | `int64` | Identifier | No | Unique Parliamentary Constituency identification code. | National ECI constituency ID. |
| **`st_code`** | `int64` | Integer / Text | No | State Census / ECI numerical code. | Standard state identifier. |
| **`st_name`** | `str` | Text | No | Name of the State or Union Territory. | e.g., UTTAR PRADESH, MAHARASHTRA, TAMIL NADU. |
| **`pc_no`** | `int64` | Dimensionless / Text | No | Attribute field 'pc_no' representing record properties in Lok Sabha Parliamentary Constituencies (2019). | Inspect 'pc_no' values for querying and filtering features in Lok Sabha Parliamentary Constituencies (2019). |
| **`pc_name`** | `str` | Text | No | Official English name of the Lok Sabha Parliamentary Constituency. | e.g., Varanasi, Gandhinagar, Wayanad, South Chennai. |
| **`pc_name_hi`** | `str` | Dimensionless / Text | No | Attribute field 'pc_name_hi' representing record properties in Lok Sabha Parliamentary Constituencies (2019). | Inspect 'pc_name_hi' values for querying and filtering features in Lok Sabha Parliamentary Constituencies (2019). |
| **`pc_category`** | `str` | Categorical (GEN, SC, ST) | ⭐ Yes | Constituency reservation status under the Constitution of India. | GEN = Open General Category, SC = Scheduled Caste Reserved, ST = Scheduled Tribe Reserved. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of Lok Sabha Parliamentary Constituencies (2019)). |
| **`wikidata_qid`** | `str` | Dimensionless / Text | No | Attribute field 'wikidata_qid' representing record properties in Lok Sabha Parliamentary Constituencies (2019). | Inspect 'wikidata_qid' values for querying and filtering features in Lok Sabha Parliamentary Constituencies (2019). |
| **`status`** | `object` | Dimensionless / Text | No | Attribute field 'status' representing record properties in Lok Sabha Parliamentary Constituencies (2019). | Inspect 'status' values for querying and filtering features in Lok Sabha Parliamentary Constituencies (2019). |
| **`2019_election_phase`** | `int64` | Dimensionless / Text | No | Attribute field '2019_election_phase' representing record properties in Lok Sabha Parliamentary Constituencies (2019). | Inspect '2019_election_phase' values for querying and filtering features in Lok Sabha Parliamentary Constituencies (2019). |
| **`2019_election_date`** | `str` | Dimensionless / Text | No | Attribute field '2019_election_date' representing record properties in Lok Sabha Parliamentary Constituencies (2019). | Inspect '2019_election_date' values for querying and filtering features in Lok Sabha Parliamentary Constituencies (2019). |

### Table: `project_jalashay_qgis_demo_01_admin_and_portfolio_district_boun`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_01_admin_and_portfolio_district_boun. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_01_admin_and_portfolio_district_boun. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`Name`** | `str` | Dimensionless / Text | ⭐ Yes | Attribute field 'Name' representing record properties in District Boundaries (All India - 734 Districts). | Inspect 'Name' values for querying and filtering features in District Boundaries (All India - 734 Districts). (PRIMARY THEMATIC KEY: used for standard cartographic categorization of District Boundaries (All India - 734 Districts)). |
| **`altitudeMo`** | `str` | Dimensionless / Text | No | Attribute field 'altitudeMo' representing record properties in District Boundaries (All India - 734 Districts). | Inspect 'altitudeMo' values for querying and filtering features in District Boundaries (All India - 734 Districts). |
| **`begin`** | `str` | Dimensionless / Text | No | Attribute field 'begin' representing record properties in District Boundaries (All India - 734 Districts). | Inspect 'begin' values for querying and filtering features in District Boundaries (All India - 734 Districts). |
| **`descriptio`** | `str` | Dimensionless / Text | No | Attribute field 'descriptio' representing record properties in District Boundaries (All India - 734 Districts). | Inspect 'descriptio' values for querying and filtering features in District Boundaries (All India - 734 Districts). |
| **`drawOrder`** | `str` | Dimensionless / Text | No | Attribute field 'drawOrder' representing record properties in District Boundaries (All India - 734 Districts). | Inspect 'drawOrder' values for querying and filtering features in District Boundaries (All India - 734 Districts). |
| **`end`** | `str` | Dimensionless / Text | No | Attribute field 'end' representing record properties in District Boundaries (All India - 734 Districts). | Inspect 'end' values for querying and filtering features in District Boundaries (All India - 734 Districts). |
| **`extrude`** | `int64` | Dimensionless / Text | No | Attribute field 'extrude' representing record properties in District Boundaries (All India - 734 Districts). | Inspect 'extrude' values for querying and filtering features in District Boundaries (All India - 734 Districts). |
| **`icon`** | `str` | Dimensionless / Text | No | Attribute field 'icon' representing record properties in District Boundaries (All India - 734 Districts). | Inspect 'icon' values for querying and filtering features in District Boundaries (All India - 734 Districts). |
| **`id`** | `str` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_01_admin_and_portfolio_district_boun. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`snippet`** | `str` | Dimensionless / Text | No | Attribute field 'snippet' representing record properties in District Boundaries (All India - 734 Districts). | Inspect 'snippet' values for querying and filtering features in District Boundaries (All India - 734 Districts). |
| **`tessellate`** | `int64` | Dimensionless / Text | No | Attribute field 'tessellate' representing record properties in District Boundaries (All India - 734 Districts). | Inspect 'tessellate' values for querying and filtering features in District Boundaries (All India - 734 Districts). |
| **`timestamp`** | `str` | Dimensionless / Text | No | Attribute field 'timestamp' representing record properties in District Boundaries (All India - 734 Districts). | Inspect 'timestamp' values for querying and filtering features in District Boundaries (All India - 734 Districts). |
| **`visibility`** | `int64` | Dimensionless / Text | No | Attribute field 'visibility' representing record properties in District Boundaries (All India - 734 Districts). | Inspect 'visibility' values for querying and filtering features in District Boundaries (All India - 734 Districts). |

### Table: `project_jalashay_qgis_demo_01_admin_and_portfolio_india_village`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_01_admin_and_portfolio_india_village. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_01_admin_and_portfolio_india_village. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`village`** | `str` | Text | No | Revenue village name. | Official Census village name. |
| **`vlcode`** | `str` | Text / Integer | No | Census 2011 Village Identification Code. | Unique national code joining with Census 2011 socioeconomic tables. |
| **`block`** | `str` | Text | No | Sub-district administrative block name. | Tehsil / Block unit. |
| **`subdistric`** | `str` | Text | No | Sub-district / Taluk name. | Sub-district unit. |
| **`district`** | `str` | Text | ⭐ Yes | District name containing the assessment block. | District level grouping. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of Revenue Village Boundaries (All India - 483k)). |
| **`Village_area`** | `float64` | Hectares (ha) / km² | No | Total geographical boundary area of the revenue village. | Total village territory. |
| **`MaxCropArea`** | `float64` | Hectares (ha) | No | Maximum net cropped area detected via multi-temporal satellite NDVI time series. | Maximum productive agricultural land extent in the village. |
| **`CropPercent`** | `float64` | Percentage (%) | No | Percentage of total village area under active crop cultivation. | CropPercent > 70% indicates heavily agricultural village; < 20% indicates forest/arid/barren terrain. |
| **`MeanCI`** | `float64` | Index / Ratio | No | Mean Cropping Intensity index (Gross Cropped Area / Net Sown Area). | MeanCI > 1.5 indicates multi-cropping (Kharif + Rabi + Zaid); ~1.0 indicates single rainfed crop. |
| **`threshKharif`** | `float64` | Precipitation Threshold (mm) | No | Calculated monsoon water requirement threshold for successful Kharif crop maturity. | Minimum rainfall needed during June-September monsoon to avoid crop failure. |
| **`threshRabi`** | `float64` | Dimensionless / Text | No | Attribute field 'threshRabi' representing record properties in Revenue Village Boundaries (All India - 483k). | Inspect 'threshRabi' values for querying and filtering features in Revenue Village Boundaries (All India - 483k). |
| **`Irr_access`** | `str` | Categorical Rank | No | Index of village access to irrigation infrastructure (Canals, Tube Wells, Tanks). | Very low, Low, Moderate, High, Very high. |
| **`avg_kharif_dev`** | `float64` | Dimensionless / Text | No | Attribute field 'avg_kharif_dev' representing record properties in Revenue Village Boundaries (All India - 483k). | Inspect 'avg_kharif_dev' values for querying and filtering features in Revenue Village Boundaries (All India - 483k). |
| **`Kharif_res`** | `str` | Categorical Rank | No | Agricultural resilience to drought stress during Kharif monsoon season. | Resilience rating based on soil moisture and supplemental water sources. |
| **`avg_rabi_dev`** | `float64` | Dimensionless / Text | No | Attribute field 'avg_rabi_dev' representing record properties in Revenue Village Boundaries (All India - 483k). | Inspect 'avg_rabi_dev' values for querying and filtering features in Revenue Village Boundaries (All India - 483k). |
| **`Rabi_res`** | `str` | Categorical Rank | No | Agricultural resilience during dry winter Rabi season (groundwater dependent). | Villages with 'Very low' Rabi resilience suffer severe winter groundwater shortages. |

### Table: `project_jalashay_qgis_demo_01_admin_and_portfolio_panchayat_bou`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_01_admin_and_portfolio_panchayat_bou. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_01_admin_and_portfolio_panchayat_bou. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`id`** | `str` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_01_admin_and_portfolio_panchayat_bou. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`ADI 2011`** | `float64` | Dimensionless / Text | No | Attribute field 'ADI 2011' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'ADI 2011' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`ADI 2019`** | `float64` | Dimensionless / Text | No | Attribute field 'ADI 2019' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'ADI 2019' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`District c`** | `int64` | Dimensionless / Text | No | Attribute field 'District c' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'District c' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`District n`** | `str` | Dimensionless / Text | No | Attribute field 'District n' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'District n' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`Female_Ill`** | `float64` | Persons (Count) | No | Number of illiterate females in the Gram Panchayat. | Socioeconomic vulnerability metric. |
| **`Female_Lit`** | `float64` | Persons (Count) | ⭐ Yes | Number of literate females in the Gram Panchayat. | Female literacy and socioeconomic development baseline. |
| **`Female_SC_`** | `float64` | Persons (Count) | No | Scheduled Caste (SC) female population. | Social equity and targeted welfare analysis. |
| **`Female_ST_`** | `float64` | Persons (Count) | No | Scheduled Tribe (ST) female population. | Tribal water rights and forest catchment community analysis. |
| **`Male_Illit`** | `float64` | Persons (Count) | No | Number of illiterate males in the Gram Panchayat. | Socioeconomic vulnerability metric. |
| **`Male_Liter`** | `float64` | Persons (Count) | No | Number of literate males in the Gram Panchayat. | Male literacy baseline. |
| **`Male_SC_Po`** | `float64` | Persons (Count) | No | Scheduled Caste (SC) male population. | Social equity and targeted welfare analysis. |
| **`Male_ST_Po`** | `float64` | Persons (Count) | No | Scheduled Tribe (ST) male population. | Tribal water rights and forest catchment community analysis. |
| **`Number_of_`** | `float64` | Dimensionless / Text | No | Attribute field 'Number_of_' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'Number_of_' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`Panchaya_1`** | `str` | Dimensionless / Text | No | Attribute field 'Panchaya_1' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'Panchaya_1' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`Panchayat_`** | `int64` | Dimensionless / Text | No | Attribute field 'Panchayat_' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'Panchayat_' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`State cens`** | `int64` | Dimensionless / Text | No | Attribute field 'State cens' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'State cens' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`State name`** | `str` | Dimensionless / Text | ⭐ Yes | Attribute field 'State name' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'State name' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). (PRIMARY THEMATIC KEY: used for standard cartographic categorization of Gram Panchayat Boundaries (All India - 183k)). |
| **`Subdistric`** | `str` | Dimensionless / Text | No | Attribute field 'Subdistric' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'Subdistric' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`Sudistrict`** | `int64` | Dimensionless / Text | No | Attribute field 'Sudistrict' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'Sudistrict' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`Total_Fema`** | `float64` | Dimensionless / Text | No | Attribute field 'Total_Fema' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'Total_Fema' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`Total_Illi`** | `float64` | Dimensionless / Text | No | Attribute field 'Total_Illi' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'Total_Illi' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`Total_Lite`** | `float64` | Dimensionless / Text | No | Attribute field 'Total_Lite' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'Total_Lite' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`Total_Male`** | `float64` | Persons (Count) | No | Total male population in the Gram Panchayat. | Demographic sex structure analysis. |
| **`Total_Popu`** | `float64` | Persons (Count) | ⭐ Yes | Total human population residing within the Gram Panchayat according to the official Indian Census. | Use for local rural drinking water demand calculation and per-capita water stress analysis. |
| **`Total_SC_P`** | `float64` | Dimensionless / Text | No | Attribute field 'Total_SC_P' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'Total_SC_P' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`Total_ST_P`** | `float64` | Dimensionless / Text | No | Attribute field 'Total_ST_P' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'Total_ST_P' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`layer`** | `str` | Dimensionless / Text | No | Attribute field 'layer' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'layer' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |
| **`path`** | `str` | Dimensionless / Text | No | Attribute field 'path' representing record properties in Gram Panchayat Boundaries (All India - 183k). | Inspect 'path' values for querying and filtering features in Gram Panchayat Boundaries (All India - 183k). |

### Table: `project_jalashay_qgis_demo_01_admin_and_portfolio_state_boundar`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_01_admin_and_portfolio_state_boundar. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_01_admin_and_portfolio_state_boundar. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`id`** | `str` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_01_admin_and_portfolio_state_boundar. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`Name`** | `str` | Dimensionless / Text | ⭐ Yes | Attribute field 'Name' representing record properties in State & UT Boundaries (All India). | Inspect 'Name' values for querying and filtering features in State & UT Boundaries (All India). (PRIMARY THEMATIC KEY: used for standard cartographic categorization of State & UT Boundaries (All India)). |

### Table: `project_jalashay_qgis_demo_06_hydrography_stage_of_groundwater_`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_06_hydrography_stage_of_groundwater_. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_06_hydrography_stage_of_groundwater_. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`id`** | `str` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_06_hydrography_stage_of_groundwater_. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`agwd_dom_i`** | `float64` | Billion Cubic Meters (BCM) / Ham | No | Annual Groundwater Extraction for Domestic and Industrial uses. | Drinking and municipal supply allocation. |
| **`agwd_irr`** | `float64` | Billion Cubic Meters (BCM) / Ham | No | Annual Groundwater Extraction specifically for Agricultural Irrigation. | Agriculture accounts for ~89% of total extraction in India. |
| **`agwd_tot`** | `float64` | Billion Cubic Meters (BCM) / Ham | No | Annual Total Groundwater Extraction Draft across all sectors (Domestic, Industrial, Agricultural). | Total groundwater extracted per year. |
| **`ar_gwr_tot`** | `float64` | Billion Cubic Meters (BCM) / Ham | No | Total Annual Replenishable Groundwater Recharge. | Total annual recharge from monsoon rainfall and irrigation return flows. |
| **`block`** | `str` | Text | No | Sub-district administrative block name. | Tehsil / Block unit. |
| **`class`** | `str` | Categorical | ⭐ Yes | Detailed functional class tag. | power_line, breakwater, generator, power_tower, toll_booth. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of Stage of Groundwater Extraction (CGWB Assessment Units)). |
| **`code`** | `float64` | Integer | No | Numerical code representing the extraction classification category. | 1 = Safe, 2 = Semi-Critical, 3 = Critical, 4 = Over-Exploited, -1 = Saline, -9999 = Not Assessed. |
| **`district`** | `str` | Text | No | District name containing the assessment block. | District level grouping. |
| **`gwr_2011_2`** | `float64` | Dimensionless / Text | No | Attribute field 'gwr_2011_2' representing record properties in Stage of Groundwater Extraction (CGWB Assessment Units). | Inspect 'gwr_2011_2' values for querying and filtering features in Stage of Groundwater Extraction (CGWB Assessment Units). |
| **`na_gwa`** | `float64` | Billion Cubic Meters (BCM) / Ham | No | Net Annual Groundwater Availability for future developmental use. | Remaining safe extraction budget available without over-exploiting the aquifer. |
| **`nat_discha`** | `float64` | Dimensionless / Text | No | Attribute field 'nat_discha' representing record properties in Stage of Groundwater Extraction (CGWB Assessment Units). | Inspect 'nat_discha' values for querying and filtering features in Stage of Groundwater Extraction (CGWB Assessment Units). |
| **`objectid`** | `int64` | Dimensionless / Text | No | Attribute field 'objectid' representing record properties in Stage of Groundwater Extraction (CGWB Assessment Units). | Inspect 'objectid' values for querying and filtering features in Stage of Groundwater Extraction (CGWB Assessment Units). |
| **`sgw_dev_pe`** | `float64` | Dimensionless / Text | No | Attribute field 'sgw_dev_pe' representing record properties in Stage of Groundwater Extraction (CGWB Assessment Units). | Inspect 'sgw_dev_pe' values for querying and filtering features in Stage of Groundwater Extraction (CGWB Assessment Units). |
| **`st_area(sh`** | `float64` | Dimensionless / Text | No | Attribute field 'st_area(sh' representing record properties in Stage of Groundwater Extraction (CGWB Assessment Units). | Inspect 'st_area(sh' values for querying and filtering features in Stage of Groundwater Extraction (CGWB Assessment Units). |
| **`st_length(`** | `float64` | Dimensionless / Text | No | Attribute field 'st_length(' representing record properties in Stage of Groundwater Extraction (CGWB Assessment Units). | Inspect 'st_length(' values for querying and filtering features in Stage of Groundwater Extraction (CGWB Assessment Units). |
| **`state`** | `str` | Text | No | State where the water project is located. | State location. |
| **`tehsil`** | `str` | Dimensionless / Text | No | Attribute field 'tehsil' representing record properties in Stage of Groundwater Extraction (CGWB Assessment Units). | Inspect 'tehsil' values for querying and filtering features in Stage of Groundwater Extraction (CGWB Assessment Units). |

### Table: `project_jalashay_qgis_demo_07_soils_and_geology_glim_india_lith`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_07_soils_and_geology_glim_india_lith. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_07_soils_and_geology_glim_india_lith. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`raw_lith`** | `str` | 2-Letter Code | No | Standard international 2-letter GLiM lithology code. | su (unconsolidated), ss (sandstone), sc (carbonate), sm (mixed), vb (basalt), vi (andesite), pa (granitoid), pb (gabbro), mt (metamorphic), ev (evaporite), wb (water). |
| **`lith_class`** | `str` | Categorical Rock Class | ⭐ Yes | Global Lithological Map (GLiM) Rock Classification (Hartmann & Moosdorf 2012). | Unconsolidated Sediment, Siliciclastic Sediments (Sandstone), Carbonate Sedimentary (Limestone), Mixed Sedimentary, Basic Volcanics (Basalt), Intermediate Volcanics, Acid Plutonics (Granite), Basic Plutonics, Metamorphic Complex, Evaporites, Water Bodies. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of GLiM India Lithology & Formations). |
| **`aquifer_score`** | `int64` | Score (-99 to 3) | No | Estimated groundwater yield / permeability rating of the rock formation. | 3 = Highly productive, 2 = Moderately productive, 1 = Low yield fractured rock, -1 = Impermeable/saline risk. |
| **`aquifer_context`** | `int64` | Integer Code | No | Hydrogeological context code relating rock type to groundwater permeability. | 1 = High porosity alluvium, 2 = Karst limestone, 3 = Sandstone, 4 = Basalt fractures, 6 = Evaporites, -1 = Low permeability. |
| **`aquifer_label`** | `str` | Text | No | Descriptive hydrogeological interpretation label for the rock formation. | Plain-English explanation of aquifer behavior (e.g., 'Volcanic / basalt-fracture aquifer context', 'Porous alluvial sediment'). |

### Table: `project_jalashay_qgis_demo_aquifers_aquifers`

| Column Name | Type | Unit | Key? | Semantic Definition | AI / Analysis Guide |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **`fid`** | `int64` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_aquifers_aquifers. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`geom`** | `object` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_aquifers_aquifers. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`id`** | `str` | Database Key / Geometry | No | Primary unique spatial database identifier / geometry blob for project_jalashay_qgis_demo_aquifers_aquifers. | Use for indexing and exact feature identification; do not use as a physical domain variable. |
| **`Age`** | `str` | Geological Era / Period | No | Geological chronological age of the aquifer formation. | Quaternary (youngest alluvial), Mesozoic, Proterozoic, Archaean (oldest crystalline basement). |
| **`Lithology_`** | `float64` | Categorical Lithology | No | Predominant lithological rock characteristics of the aquifer matrix. | Porous sedimentary vs fractured crystalline. |
| **`Major_Aq_1`** | `str` | Dimensionless / Text | No | Attribute field 'Major_Aq_1' representing record properties in Principal Aquifers of India (CGWB). | Inspect 'Major_Aq_1' values for querying and filtering features in Principal Aquifers of India (CGWB). |
| **`Major_Aqui`** | `str` | Categorical Aquifer Group | No | Broad hydrogeological group (Unconsolidated, Semi-consolidated, Fissured Hard Rock). | Key division between high-yielding porous alluvial basins and low-storage fractured hard rocks. |
| **`Principal_`** | `str` | Categorical Rock Formation | ⭐ Yes | Major Principal Aquifer System classified by CGWB hydrogeologists. | Alluvium (unconsolidated), Basalt/Deccan Traps (fissured), Banded Gneissic Complex, Granite, Sandstone, Limestone (Karst), Schist, Laterite, Shale, Quartzite, Charnockite. (PRIMARY THEMATIC KEY: used for standard cartographic categorization of Principal Aquifers of India (CGWB)). |
| **`Recommende`** | `float64` | Dimensionless / Text | No | Attribute field 'Recommende' representing record properties in Principal Aquifers of India (CGWB). | Inspect 'Recommende' values for querying and filtering features in Principal Aquifers of India (CGWB). |
| **`aquifer`** | `str` | Dimensionless / Text | No | Attribute field 'aquifer' representing record properties in Principal Aquifers of India (CGWB). | Inspect 'aquifer' values for querying and filtering features in Principal Aquifers of India (CGWB). |
| **`aquifer0`** | `str` | Dimensionless / Text | No | Attribute field 'aquifer0' representing record properties in Principal Aquifers of India (CGWB). | Inspect 'aquifer0' values for querying and filtering features in Principal Aquifers of India (CGWB). |
| **`aquifers`** | `str` | Dimensionless / Text | No | Attribute field 'aquifers' representing record properties in Principal Aquifers of India (CGWB). | Inspect 'aquifers' values for querying and filtering features in Principal Aquifers of India (CGWB). |
| **`area_re`** | `float64` | Dimensionless / Text | No | Attribute field 'area_re' representing record properties in Principal Aquifers of India (CGWB). | Inspect 'area_re' values for querying and filtering features in Principal Aquifers of India (CGWB). |
| **`avg_mbgl`** | `str` | Meters Below Ground Level (m bgl) | No | Average historical depth to water table in meters below ground level. | Range of groundwater depth; >20 m bgl indicates deep water stress; <5 m bgl indicates shallow water table. |
| **`m2_perday`** | `str` | Square Meters per Day (m²/day) | ⭐ Yes | Aquifer Transmissivity (T = K * b), the rate at which water is transmitted through a unit width of the aquifer under a unit hydraulic gradient. | High values (>1,000 m²/day) indicate high-yielding alluvial aquifer systems in Indo-Gangetic and coastal plains. Low values (<50 m²/day) indicate tight crystalline hard rock. |
| **`m3_per_day`** | `str` | Cubic Meters per Day (m³/day) | ⭐ Yes | Estimated Well Yield Potential per tube well or bore well under standard operating drawdown. | High yields (>1,500 m³/day) support heavy agricultural irrigation tube wells. Low yields (<100 m³/day) are limited to shallow domestic dugwells. |
| **`mbgl`** | `str` | Dimensionless / Text | No | Attribute field 'mbgl' representing record properties in Principal Aquifers of India (CGWB). | Inspect 'mbgl' values for querying and filtering features in Principal Aquifers of India (CGWB). |
| **`newcode14`** | `str` | Dimensionless / Text | No | Attribute field 'newcode14' representing record properties in Principal Aquifers of India (CGWB). | Inspect 'newcode14' values for querying and filtering features in Principal Aquifers of India (CGWB). |
| **`newcode43`** | `str` | Dimensionless / Text | No | Attribute field 'newcode43' representing record properties in Principal Aquifers of India (CGWB). | Inspect 'newcode43' values for querying and filtering features in Principal Aquifers of India (CGWB). |
| **`objectid`** | `float64` | Dimensionless / Text | No | Attribute field 'objectid' representing record properties in Principal Aquifers of India (CGWB). | Inspect 'objectid' values for querying and filtering features in Principal Aquifers of India (CGWB). |
| **`pa_order`** | `float64` | Integer Rank | No | Hydrogeological priority ordering rank assigned by CGWB. | Rank from 1 to 15 for standardized mapping display. |
| **`per_cm`** | `str` | Kilograms / Seconds / Specific Capacity | No | Hydraulic Conductivity / Specific Capacity permeability index of the aquifer matrix. | Used in pumping test evaluations and draw-down cone analysis. |
| **`shape_Area`** | `float64` | Dimensionless / Text | No | Attribute field 'shape_Area' representing record properties in Principal Aquifers of India (CGWB). | Inspect 'shape_Area' values for querying and filtering features in Principal Aquifers of India (CGWB). |
| **`shape_Leng`** | `float64` | Dimensionless / Text | No | Attribute field 'shape_Leng' representing record properties in Principal Aquifers of India (CGWB). | Inspect 'shape_Leng' values for querying and filtering features in Principal Aquifers of India (CGWB). |
| **`state`** | `str` | Text | No | State where the water project is located. | State location. |
| **`system`** | `str` | Categorical | No | Aquifer system structure: Single unconfined, Multiple semi-confined/confined, or Unexplored. | Indicates whether deep multi-layered confined aquifers exist below the shallow water table. |
| **`test`** | `str` | Dimensionless / Text | No | Attribute field 'test' representing record properties in Principal Aquifers of India (CGWB). | Inspect 'test' values for querying and filtering features in Principal Aquifers of India (CGWB). |
| **`yeild__`** | `str` | Percentage (%) | ⭐ Yes | Aquifer Storativity / Specific Yield (Sy), representing the ratio of the volume of water that saturated aquifer material will yield by gravity to the total volume of material. | High Specific Yield (8-20%) represents unconsolidated sand and gravel aquifers. Low Storativity (Upto 1-3%) represents fractured crystalline basement rocks. |
| **`zone_m`** | `str` | Meters (m) | No | Effective saturated aquifer thickness / depth interval zone in meters below ground level. | Used to calculate total groundwater storage volume (Storage = Area * Thickness * Sy). |