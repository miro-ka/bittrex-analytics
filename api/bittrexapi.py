import logging
import pandas as pd
import urllib.request
import json


class BittrexAPI:
    logger = logging.getLogger(__name__)
    # URL'S
    get_currencies_url = "https://bittrex.com/api/v1.1/public/getcurrencies"

    def __init__(self):
        self.logger.info('logging on')

    def get_currencies(self):
        """
        :return: All Bittrex currencies as Pandas DataFrame
        """
        response = urllib.request.urlopen(self.get_currencies_url)
        data = json.loads(response.read())
        data_res_json = data['result']
        df = pd.DataFrame(data_res_json)
        return df
