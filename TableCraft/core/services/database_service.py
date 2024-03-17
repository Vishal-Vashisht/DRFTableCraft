from sqlalchemy import create_engine
from abc import ABC, abstractmethod
from urllib.parse import quote


class DataBase(ABC):

    @abstractmethod
    def connect(self):
        pass


class PostgreSQL(DataBase):

    def __init__(self, connection_url) -> None:
        self.connection_url = connection_url

    def connect(self):
        try:
            self.sql_engine = create_engine(self.connection_url)
            self.connection = self.sql_engine.connect()
        except Exception as exce:
            raise exce


"""
This class handle the configuration of the database connection

"""


class DatabaseConfigurator(ABC):

    @abstractmethod
    def db_create_engine(self):
        pass


class PostgreSQLConfigurator(DatabaseConfigurator):

    def __init__(self, data) -> None:

        self.user = data.get("user")
        self.host = data.get("host")
        self.password = data.get("password")
        self.db_name = data.get("db_name")
        self.port = data.get("port")

    def db_create_engine(self):
        try:
            connection_url = f'postgresql+psycopg2://{self.user}:{quote(self.password.encode())}@{self.host}:{self.port}/{self.db_name}' # noqa
            create_engine(connection_url)
            return connection_url
        except Exception as exec:
            raise exec
