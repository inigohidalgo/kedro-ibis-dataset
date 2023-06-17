import os
import pytest

import duckdb
from kedro.io import DataCatalog
import pandas as pd
from pandas.testing import assert_frame_equal

from kedro_ibis_dataset import IbisDataSet

@pytest.fixture
def temp_db_connection_string(tmp_path):
    """Fixture to create a temporary database."""
    db_path = tmp_path / 'test.db'
    duckdb_conn_str = f'duckdb://{db_path}'
    # Setup: create a temporary database
    os.makedirs(tmp_path, exist_ok=True)
    con = duckdb.connect(str(db_path))
    con.close()
    credentials = {'con': duckdb_conn_str}
    yield credentials
    # Teardown: delete the temporary database
    if os.path.exists(db_path):
        os.remove(db_path)

@pytest.fixture
def dummy_dataframe():
    """Fixture to create a dummy dataframe."""
    return pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

class TestIbisDataSet:
    def test_save_and_load(self, temp_db_connection_string, dummy_dataframe):
        """Test saving and reloading the data."""
        table_name = 'test_table'
        credentials = temp_db_connection_string
        data = IbisDataSet(table_name, credentials=credentials)
        data.save(dummy_dataframe)
        reloaded = data.load().to_pandas()
        assert_frame_equal(dummy_dataframe, reloaded)

    def test_insert_existing_table(self, temp_db_connection_string, dummy_dataframe):
        """Test saving and reloading the data."""
        table_name = 'test_table'
        credentials = temp_db_connection_string
        data = IbisDataSet(table_name, credentials=credentials)
        data.save(dummy_dataframe)
        data.save(dummy_dataframe)
        reloaded = data.load().to_pandas()
        assert_frame_equal(pd.concat([dummy_dataframe, dummy_dataframe]).reset_index(drop=True), reloaded.reset_index(drop=True))
    # TODO: test overwrite vs append

    def test_insert_existing_table_overwrite(self, temp_db_connection_string, dummy_dataframe):
        """Test saving and reloading the data."""
        table_name = 'test_table'
        credentials = temp_db_connection_string
        save_args = {'overwrite': True}
        data = IbisDataSet(table_name, save_args=save_args, credentials=credentials)
        data.save(dummy_dataframe)
        data.save(dummy_dataframe)
        reloaded = data.load().to_pandas()
        assert_frame_equal(dummy_dataframe, reloaded)
