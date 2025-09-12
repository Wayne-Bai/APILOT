import pandas as pd
from pandas.api.types import is_datetime64_any_dtype as is_datetime

def from_tuples(data, freq=None, closed=None, name=None):
    """
    Construct an IntervalIndex from an array-like of tuples.

    Parameters
    ----------
    data : array-like, list-like, tuple, or list of tuples
        The data to construct an IntervalIndex from.
    freq : str or DateOffset, optional
        The frequency of the intervals in the resulting Index.
    closed : {'left', 'right', 'both', 'neither'}, default 'right'
        Make the interval closed with respect to the given frequency to
        the 'left', 'right', 'both', or 'neither' sides.
    name : str, optional
        The name of the resulting index.

    Returns
    -------
    pandas.IntervalIndex

    Examples
    --------
    >>> pd.IntervalIndex.from_tuples([(0, 1), (1, 4), (4, 5)])
    IntervalIndex([(0, 1], (1, 4], (4, 5]],
                  closed='right', dtype='interval[ns]')

    >>> pd.IntervalIndex.from_tuples([(0, 1), (1, 4), (4, 5)],
    ...                              closed='left')
    IntervalIndex([(0, 1], (1, 4], (4, 5]],
                  closed='left', dtype='interval[ns]')
    """
    data = np.asarray(data)
    if is_datetime(data.dtype):
        data = tslibs.timedeltas.to_timedelta(data)
    return pd.IntervalIndex(data, freq=freq, closed=closed, name=name)
