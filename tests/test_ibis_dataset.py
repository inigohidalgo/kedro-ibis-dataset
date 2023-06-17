import os
import pytest

from kedro.io import DataCatalog
import duckdb

from kedro_ibis_dataset import IbisDataSet

@pytest.fixture
def temp_db(tmp_path):
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

class TestIbisDataSet:
    def test_save_and_load(self, temp_db):
        """Test saving and reloading the data."""
        table_name = 'test_table'
        credentials = temp_db
        data = IbisDataSet(table_name, credentials)
        data.save('test')
        reloaded = data.load()
        assert reloaded == 'test'