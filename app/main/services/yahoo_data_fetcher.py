from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import yfinance as yf


@dataclass
class YahooDataFetcher:

    code: str
    start: datetime
    end: datetime
    ticker: Optional[yf.Ticker]

    def __post_init__(self):
        if not self.ticker:
            self.ticker = yf.Ticker(ticker=self.code)

    def get_last_week(self):
        """
        get the ticker stock data in the last 5 days
        """
        hist_df = self.ticker.history("5d")
        return hist_df.T.to_dict()
