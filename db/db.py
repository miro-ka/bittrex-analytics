import logging
import sqlite3
import pandas as pd


class DB:
    logger = logging.getLogger(__name__)
    # URL'S
    db_file = "db/bittrex-analytics.sqlite"

    def __init__(self):
        self.logger.info("Starting db client")
        self.conn = sqlite3.connect(self.db_file)
        self.logger.info("Starting db client - done")

    def get_all_currencies(self):
        """
        :return: All Bittrex currencies from sql as Pandas DataFrame
        """
        try:
            df = pd.read_sql_query("select * from currencies;", self.conn)
            return df
        except pd.io.sql.DatabaseError as e:
            self.logger.warning("DatabaseError: Table currencies most probably does not exist")
            return None

    def store_currencies(self, df):
        """
        Stores pandas dataFrame to sql-lite
        """
        self.logger.info("Storing new currencies table data")
        df.to_sql("currencies", self.conn, if_exists="replace", index=False)
        self.logger.info("Storing new currencies table data - done")
        return True
