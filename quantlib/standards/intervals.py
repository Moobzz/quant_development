import pytz
from enum import Enum


class Period(Enum):
    SECOND = "s"
    MINUTE = "m"
    HOURLY = "h"
    DAILY = "d"
    WEEKLY = "w"
    MONTHLY = "M"
    YEARLY = "y"


str_to_period = {member.value: member for member in Period}
# print(str_to_period)

# get_trade_bars(
#     granularity=Period.MINUTE
# )
