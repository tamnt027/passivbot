from numba import types, typed, njit
from numba.experimental import jitclass


@jitclass([
    ('timestamp', types.int64),
    ('open', types.float64),
    ('high', types.float64),
    ('low', types.float64),
    ('close', types.float64),
    ('qty', types.float64)
])
class Candle:
    """
    A class representing a candle.
    """

    def __init__(self, timestamp: int, open: float, high: float, low: float, close: float, qty: float):
        """
        Creates a candle.
        :param timestamp: The timestamp of the candle.
        :param open: The open price of the candle.
        :param high: The highest price of the candle.
        :param low: The lowest price of the candle.
        :param close: The close price of the candle.
        :param qty: The quantity of the candle.
        """
        self.timestamp = timestamp
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.qty = qty


@njit
def empty_candle_list():
    l = typed.List()
    l.append(Candle(0, 0.0, 0.0, 0.0, 0.0, 0.0))
    l.clear()
    return l
