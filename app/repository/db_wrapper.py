import mysql.connector.pooling
from mysql.connector import MySQLConnection


class Pool:
    def __init__(self, db_config) -> None:
        super().__init__()
        self.pool = mysql.connector.pooling.MySQLConnectionPool(pool_name='mysql_pool',
                                                                pool_size=20,
                                                                auth_plugin='mysql_native_password',
                                                                **db_config)
        self.get_connection()

    def get_connection(self) -> MySQLConnection:
        return self.pool.get_connection()
