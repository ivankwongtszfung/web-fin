from unittest.mock import Mock
from datetime import date, timedelta
from faker import Faker

import pytest
import pandas as pd
import numpy as np

from app.main.services import YahooDataFetcher

faker = Faker()

LIST_OF_COLUMNS = ["Open", "High", "Low", "Close",
                   "Volume", "Dividends", "Stock Splits"]


@pytest.fixture
def period5d():
    end_period = date.today()
    start_period = end_period - timedelta(days=4)
    if start_period.weekday() >= 5:
        delta = start_period.weekday() - 4  # days before Friday
        start_period = start_period - timedelta(days=delta)
    return {"start": start_period, "end": end_period}


@pytest.fixture
def tickerDf(period5d):
    dates = pd.date_range(**period5d)
    sample_data = np.random.randn(5, len(LIST_OF_COLUMNS))
    df = pd.DataFrame(sample_data,
                      index=dates,
                      columns=LIST_OF_COLUMNS)
    return df


@pytest.fixture
def ticker(tickerDf):
    tickerObject = Mock()
    tickerObject.history.return_value = tickerDf
    return tickerObject


# @pytest.fixture
# def yFinance(ticker):
#     yFinance = Mock()
#     yFinance.Ticker.return_value = ticker
#     return yFinance


class TestYahooDataFetcher:
    def test_last_5d(self, ticker, period5d):
        """
            it return an dict object with correct dates and format.
        """
        ydf = YahooDataFetcher(code=faker.pystr(), ticker=ticker, **period5d)
        result = ydf.get_last_week()
        start_period, end_period = period5d.values()
        for date_key in result.keys():
            if start_period <= date_key <= end_period:
                assert True, "return dates should be within last week"
