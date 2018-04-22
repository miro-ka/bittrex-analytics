import sys
import logging
from analytics.analytics import Analytics
from report.report import Report


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)
#report = Report("YOUR_EMAIL", "YOUR_PASSWORD", "RECIPIENTS_PASSWORD")


def get_new_currencies():
    """
    Handles new currencies
    """
    analytics = Analytics()
    new_currencies = analytics.get_new()
    if new_currencies is None:
        return None

    body = ""
    for index, row in new_currencies.iterrows():
        body += row.Currency + " (" + row.CurrencyLong + " )"
        body += "\n"
    report.add("New Currencies:", body)


def main():
    logger.info("info from bittrex-analytics")
    get_new_currencies()
    report.send()
    logger.info("done")


if __name__ == "__main__":
    main()
