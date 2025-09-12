
import pandas as pd

def get_fixed_frequency_datetimeindex(start_date, end_date, freq):
    """Return a fixed frequency DatetimeIndex.

    Args:
        start_date (str or datetime): Start date of the index.
        end_date (str or datetime): End date of the index.
        freq (str): Frequency string in Pandas format, e.g., 'D', 'W-FRI', etc.

    Returns:
        pd.DatetimeIndex: A fixed frequency DatetimeIndex spanning from start_date to end_date with the given frequency.
    """
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    freq = pd.tseries.frequencies.to_offset(freq)
    return pd.date_range(start=start_date, end=end_date, freq=freq)
