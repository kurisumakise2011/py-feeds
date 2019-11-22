import logging as log

import mysql.connector.pooling

from app.exception.critical_error import InternalError
from app.repository.db_wrapper import Pool


class AbstractRepository(object):

    def __init__(self, pool: Pool) -> None:
        super().__init__()
        self.pool = pool

    def execute(self, sql_query: str, parameters):
        con = None
        cursor = None
        try:
            con = self.pool.get_connection()
            cursor = con.cursor()
            cursor.execute(sql_query, parameters)
            con.commit()
            return cursor.lastrowid
        except mysql.connector.Error as e:
            log.error("%s mysql connection error occurred", e)
            raise InternalError(e)
        except TypeError as e:
            log.error("%s type error occurred", e)
            raise InternalError(e)
        finally:
            if cursor is not None:
                cursor.close()
            if con is not None:
                con.close()

    def query(self, sql_query: str, parameters, mapper):
        con = None
        cursor = None
        try:
            con = self.pool.get_connection()
            cursor = con.cursor()
            cursor.execute(sql_query, parameters)
            rs = mapper(cursor)
            if rs:
                return rs
            else:
                return []
        except mysql.connector.Error as e:
            log.error("%s mysql connection error occurred", e)
            return None
        except TypeError as e:
            log.error("%s type error occurred", e)
            return None
        finally:
            if cursor is not None:
                cursor.close()
            if con is not None:
                con.close()

    def now(self):
        cursor = None
        con = None
        try:
            con = self.pool.get_connection()
            cursor = con.cursor()
            cursor.execute("select now()")
            time = cursor.fetchone()[0]
        except mysql.connector.Error as e:
            log.error("%s mysql connection error occurred", e)
            raise RuntimeError('Cannot run application due to db failures', e)
        except TypeError as e:
            log.error("%s type error occurred", e)
            return None
        else:
            log.info("Mysql working current time is %s", time)
        finally:
            if cursor is not None:
                cursor.close()
            if con is not None:
                con.close()
