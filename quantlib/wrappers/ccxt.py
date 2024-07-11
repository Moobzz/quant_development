import pandas as pd
import pytz
from datetime import datetime


def map_to_granularity(granularity, granularity_multiplier, exchange_client):
    if (
        str(granularity_multiplier) + granularity.value
        not in exchange_client.timeframes
    ):
        raise ValueError(
            f"timeframe is not supported, requires <granularity_multiplier><granulariy> to be in {exchange_client.timeframes}"
        )
    return str(granularity_multiplier) + granularity.value


class Ccxt:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_trade_bars(
        ticker,
        start,
        end,
        granularity,
        granularity_multiplier,
        exchange_client,
    ):
        timeframe = map_to_granularity(
            granularity, granularity_multiplier, exchange_client
        )
        date_ms_timestamp = lambda x: int(x.timestamp() * 1000)
        ms_start, ms_end = date_ms_timestamp(start), date_ms_timestamp(end)
        ohlcvs = []
        while ms_start < ms_end:

            ohlcv = exchange_client.fetch_ohlcv(
                symbol="BTCUSDT",
                timeframe=timeframe,
                since=ms_start,
            )
            if ohlcv == None or len(ohlcv) == 0:
                break
            if len(ohlcvs) > 0 and ohlcv[-1][0] == ohlcvs[-1][0]:
                break
            # input((ms_start, ohlcv[-1][0]))
            if len(ohlcv) == 0:
                pass
            ms_start = ohlcv[-1][0]
            ohlcvs += ohlcv

            # print(ohlcvs)
        ohlcv = pd.DataFrame(
            data=ohlcvs,
            columns=["datetime", "open", "high", "low", "close", "volume"],
        )

        ohlcv["datetime"] = pd.to_datetime(
            ohlcv["datetime"], unit="ms", utc=True
        )
        ohlcv = ohlcv.set_index("datetime", drop=True)
        # input(ohlcv.index.duplicated(keep="first"))
        ohlcv = ohlcv[~ohlcv.index.duplicated(keep="first")]

        # print(ohlcv)
        return ohlcv
        # return data
