# Kedro IbisDataSet

Connector to load data from SQL tables into Python [Kedro](https://github.com/kedro-org/kedro) pipelines using [Ibis](https://github.com/ibis-project/ibis) tables.
This allows for connecting to databases and constructing queries dynamically using Kedro's node-pipeline framework to construct Ibis expressions.

To save data into SQL tables, the connector can save either `pandas` dataframes or `ibis` expressions.

For an example usage see [this project](https://github.com/inigohidalgo/ibis-kedro-poc/).
