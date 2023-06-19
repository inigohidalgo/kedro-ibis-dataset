# Kedro IbisDataSet

Connector to load data from SQL tables into Python [Kedro](https://github.com/kedro-org/kedro) pipelines using [Ibis](https://github.com/ibis-project/ibis) tables.
This allows for connecting to databases and constructing queries dynamically using Kedro's node-pipeline framework to construct Ibis expressions.

To save data into SQL tables, the connector can save either `pandas` dataframes or `ibis` expressions.

To initiate a DataSet, currently we must pass a connection string (`{backend}://{database-connection-string}`). See [this section of the Ibis documentation](https://ibis-project.org/blog/Ibis-version-3.1.0-release/?h=ibis.connect#ibisconnect) for more details.


## How to use

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


For an example usage see [this project](https://github.com/inigohidalgo/ibis-kedro-poc/).

For more information on how to use Ibis to connect to SQL databases see the [Ibis documentation](https://ibis-project.org/docs/).