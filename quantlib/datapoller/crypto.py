from quantlib.datapoller.base import BasePoller
from quantlib.datapoller.utils import ts_poller


class Crypto(BasePoller):
    @ts_poller
    def get_trade_bars(
        self, src, ticker, start, end, granularity, granularity_multiplier
    ):
        return self.pollers[src].get_trade_bars(
            ticker, start, end, granularity, granularity_multiplier
        )
