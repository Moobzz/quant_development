from quantlib.datapoller.master import DataPoller
from quantlib.wrappers.binance import Binance
from datetime import datetime
from quantlib.standards.intervals import Period


# bin = Binance()
# res = bin.get_trade_bars(
#     ticker="BTCUSDT",
#     start=datetime(2018, 1, 1),
#     end=datetime(2024, 1, 1),
#     granularity=Period.DAYLY,
#     granularity_multiplier="3",
# )
# print(res)
# async def main():
datapoller = DataPoller()
res = datapoller.crypto.get_trade_bars(
    src="binance",
    ticker="BTCUSDT",
    start=datetime(2018, 1, 1),
    end=datetime(2024, 1, 1),
    granularity=Period.DAYLY,
    granularity_multiplier="3",
)
# # exit()
# print(res)


# import asyncio

# asyncio.run(main())


# clients = {"binance": Binance()}

# src = "binance"
# ticker = "BTCUSDT"

# res = clients[src].get_trade_bars(
#     ticker=ticker,
#     start=datetime(2018, 1, 1),
#     end=datetime(2024, 1, 1),
#     granularity=Period.DAYLY,
#     granularity_multiplier="3",
# )
# print(res)
