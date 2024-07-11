from quantlib.datapoller import crypto


class DataPoller:

    def __init__(self, config_keys={"binance": {}}):
        src_pollers = {}
        for src, kwargs in config_keys.items():
            Wrapper_cls = None
            if src == "binance":
                from quantlib.wrappers.binance import Binance

                Wrapper_cls = Binance
            if src != "binance":
                return None
            if Wrapper_cls is not None:
                src_pollers[src] = Wrapper_cls(**kwargs)

        self.src_pollers = src_pollers
        self.crypto = crypto.Crypto(pollers=self.src_pollers)
