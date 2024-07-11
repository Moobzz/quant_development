class Binance:

    def __init__(self):
        import ccxt

        self.ccxt_client = ccxt.binance()

    # h m D
    def get_trade_bars(
        self, ticker, start, end, granularity, granularity_multiplier
    ):
        from quantlib.wrappers.ccxt import Ccxt

        return Ccxt.get_trade_bars(
            ticker=ticker,
            start=start,
            end=end,
            granularity=granularity,
            granularity_multiplier=granularity_multiplier,
            exchange_client=self.ccxt_client,
        )
