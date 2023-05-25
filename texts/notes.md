# Notes:

## Database:

### Names:

1. MainDb
   - mi_lqk_dq.csv
1. sitesDb
   - BI_mst_lq_Q.csv
1. chemDb
   - rx_param_4_lq_q.csv

### Inter connections in Dbs:

1. MainDb.idObj == siteDb.idSatz
1. MainDb.param == chemDb.idSatz

### chemicals in mainDb

| chemDb.objkey |            chemDb.objnam            | MainDb.param |
| :-----------: | :---------------------------------: | :----------: |
|      NO       |  Stickstoffmonoxid [nitric oxide]   |     2053     |
|      NO2      | Stickstoffdioxid [nitrogen dioxide] |     1369     |
|      O3       |                Ozon                 |      1       |
|     PM10      |                PM10                 |    38305     |
|      SO2      |   Schwefeldioxid[sulfur dioxide]    |     685      |
|     PM2.5     |                PM2.5                |    38989     |

> Know thresholds
