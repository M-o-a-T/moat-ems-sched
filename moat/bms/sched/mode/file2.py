import anyio
from . import Loader as _Loader
from . import BaseLoader

class Loader(BaseLoader):
    """
    Derive buy from sell price.

    This importer calculates the cost for buying energy from those of sold energy.
    """

    @staticmethod
    async def price_buy(cfg):
        """
        Read future prices for incoming energy, in $$$/kWh.
        File format: one float per line.

        Config:
            data.file2.const (float): additional fixed price per kWh.
            data.file2.factor (float): Multiplicator for the values read from the file.
        """
        factor = cfg.data.file2.factor
        offset = cfg.data.file2.offset

        async for x in _Loader(cfg.mode.price_sell).price_sell(cfg):
            yield float(x)*factor+offset