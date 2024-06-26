# Kedro IbisDataSet

This was a proof of concept designed to kickstart discussions around integrating [Ibis](https://github.com/ibis-project/ibis) and [Kedro](https://github.com/kedro-org/kedro). This functionality was merged into Kedro, refer to the [official implementation](https://github.com/kedro-org/kedro-plugins/blob/main/kedro-datasets/kedro_datasets/ibis/table_dataset.py) by @deepyaman.

----

Connector to load data from SQL tables into Python [Kedro](https://github.com/kedro-org/kedro) pipelines using [Ibis](https://github.com/ibis-project/ibis) tables.
This allows for connecting to databases and constructing queries dynamically using Kedro's node-pipeline framework to construct Ibis expressions.

To save data into SQL tables, the connector can save either `pandas` dataframes or `ibis` expressions.

To initiate a DataSet, currently we must pass a connection string (`{backend}://{database-connection-string}`). See [this section of the Ibis documentation](https://ibis-project.org/blog/Ibis-version-3.1.0-release/?h=ibis.connect#ibisconnect) for more details.


## How to use

To see an example usage in a kedro pipeline see [this project](https://github.com/inigohidalgo/ibis-kedro-poc/).

### 1. pip install the package
```bash
pip install kedro-ibis-dataset
```

### 2. Use as any other Kedro DataSet


`credentials.yml`
```yaml
database_creds:
    con: backend://connection-url
```

`catalog.yml`
```yaml
ibis_dataset_table:
  type: kedro_ibis_dataset.IbisDataSet
  table_name: table_name
  credentials: database_creds
  save_args:
    overwrite: true/false
```




For more information on how to use Ibis to connect to SQL databases see the [Ibis documentation](https://ibis-project.org/docs/).
