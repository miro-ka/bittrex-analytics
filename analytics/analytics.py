import logging
import numpy as np
from db.db import DB
from api.bittrexapi import BittrexAPI


class Analytics:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.logger.info('logging on')
        self.bittrex_api = BittrexAPI()
        self.db = DB()

    def get_new(self):
        """
        :return: Returns new currencies
        """
        # Get New currencies
        self.logger.info("Getting new currencies")
        exchange_currencies_df = self.bittrex_api.get_currencies()
        self.logger.info("Got total currencies: " + str(exchange_currencies_df.shape[0]))
        active_df = exchange_currencies_df[exchange_currencies_df['IsActive'] == True]
        self.logger.info("Active currencies: " + str(active_df.shape[0]))

        # Get DB currencies
        db_currencies_df = self.db.get_all_currencies()

        if db_currencies_df is None:
            self.logger.info("No DB currencies,..have to wait another iteration")
            self.db.store_currencies(exchange_currencies_df)
            return None

        new_currencies = np.setdiff1d(exchange_currencies_df.Currency,
                                      db_currencies_df.Currency)

        if len(new_currencies) > 0:
            new_currencies_df = exchange_currencies_df.loc[exchange_currencies_df['Currency'].isin(new_currencies)]
            #self.db.store_currencies(exchange_currencies_df)
            return new_currencies_df

        self.logger.info("No new currencies have been added to Bittrex exchange.")
        return None
