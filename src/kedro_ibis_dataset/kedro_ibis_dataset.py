from kedro.io import AbstractDataSet, DataSetError
import ibis


class IbisDataSet(AbstractDataSet):
    connections = {}

    def __init__(self, table_name, credentials):

        if not table_name:
            raise DataSetError("'table_name' argument cannot be empty.")

        if not (credentials and "con" in credentials and credentials["con"]):
            raise DataSetError("'con' argument cannot be empty. Please provide an ibis connection string.")

        self.connection_string = credentials["con"]
        self.table_name = table_name
        self.credentials = credentials
        self.create_connection(self.connection_string)

    @classmethod
    def create_connection(cls, connection_string):
        if connection_string not in cls.connections:
            cls.connections[connection_string] = ibis.connect(connection_string)
        return

    def _load(self):
        con = self.connections[self.connection_string]
        return con.table(self.table_name)

    def _save(self, data):
        raise DataSetError("Saving to IbisDataSet is not supported.")
    
    def _describe(self):
        return dict(
            table_name=self.table_name,
            credentials=self.credentials
        )
