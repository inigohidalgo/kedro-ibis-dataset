from typing import Dict

from kedro.io import AbstractDataSet, DataSetError
import ibis


class IbisDataSet(AbstractDataSet):
    """``IbisDataSet`` loads and `TODO` data to a table in an Ibis connection.
    When loading data, it returns an Ibis table which is a lazy connection to the data.
    """
    connections: Dict[str, ibis.BaseBackend] = {}

    def __init__(self, table_name: str, credentials: Dict[str, str]):
        """Creates a new instance of ``IbisDataSet`` pointing to a table in an Ibis connection.
        The connection is created only once per connection string and shared across all instances.

        Args:
            table_name: The name of the table which will be returned when loading data.
            credentials: A dictionary containing the connection string under the key "con".
        
        Raises:
            DataSetError: When ``table_name`` is empty.
        """
        if not table_name:
            raise DataSetError("'table_name' argument cannot be empty.")

        if not (credentials and "con" in credentials and credentials["con"]):
            raise DataSetError("'con' argument cannot be empty. Please provide an ibis connection string.")

        self.connection_string = credentials["con"]
        self.table_name = table_name
        self.credentials = credentials
        self.create_connection(self.connection_string)

    @classmethod
    def create_connection(cls, connection_string: str):
        """If a connection has not been created for the given connection string,
        create a new connection and store it in the class variable ``connections``.

        Args:
            connection_string: The connection string to use for creating the connection.
        
        Returns:
            None
        """
        if connection_string not in cls.connections:
            cls.connections[connection_string] = ibis.connect(connection_string)
        return



    def _load(self):
        return self._table

    def _save(self, data, **kwargs):
        if self._table_exists:
            self._table.insert(data, **kwargs)
        else:
            self._connection.create_table(self.table_name, data)

    def _describe(self):
        return dict(
            table_name=self.table_name,
            credentials=self.credentials
        )
    @property
    def _table(self):
        if not self._table_exists:
            raise DataSetError(f"Table '{self.table_name}' does not exist in DB.")
        return self._connection.table(self.table_name)

    # TODO: extend _exists for kedro funcionality?
    # is there a functional benefit with kedro?
    # def _exists(self):
    @property
    def _table_exists(self):
        return self.table_name in self._connection.list_tables()

    @property
    def _connection(self):
        return self.connections[self.connection_string]