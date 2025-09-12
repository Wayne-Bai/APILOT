
import pandas as pd

def get_quantile(data, q, axis=0):
    """
    Returns values at the given quantile over requested axis.
    
    Parameters:
        data (pandas.DataFrame or Series): The input data.
        q (float or array-like): The desired quantile or sequence of quantiles to compute.
        axis (int or str): Axis along which the quantile is computed. If None, the entire array is used.
    
    Returns:
        pandas.Series or float: The values at the given quantile over the requested axis.
    """
    if not isinstance(data, pd.DataFrame) and not isinstance(data, pd.Series):
        raise ValueError("'data' must be a pandas.DataFrame or pandas.Series")
    
    if q <= 0 or q >= 1:
        raise ValueError("'q' must be between 0 and 1")
    
    if axis is not None and (not isinstance(axis, int) and not isinstance(axis, str)):
        raise ValueError("'axis' must be an integer or a string")
    
    if data.ndim > 2:
        raise ValueError("Only 1D and 2D arrays are supported")
    
    if axis == 0 and data.shape[0] == 1:
        return data.iloc[0, :]
    elif axis == 1 and data.shape[1] == 1:
        return data.iloc[:, 0]
    else:
        return pd.Series(data.quantile(q, axis=axis))
