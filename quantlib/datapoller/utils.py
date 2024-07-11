import asyncio
import functools
from quantlib.standards.intervals import Period


def ts_poller(_func=None, *, map_span=True):
    default_args = {
        "ticker": None,
        "start": None,
        "end": None,
        "periods": None,
        "granularity": Period.DAYLY,
        "granularity_multiplier": 1,
        "src": None,
    }

    def sync_warpper(poller_obj, *arg, **kwargs):
        print(poller_obj)
        print(arg)
        print(kwargs)
        pass

    async def async_wrapper(poller_obj, *arg, **kwargs):
        print("something")
        pass

    def _wrapper(poller_func):
        if asyncio.iscoroutinefunction(poller_func):
            return async_wrapper
        else:
            return sync_warpper

    if _func is None:  # Means decorator argument is inputed
        # input(1)
        return _wrapper
    else:  # Means decorator argument is not inputed
        # input(2)
        return _wrapper(_func)
    # input(_func)
