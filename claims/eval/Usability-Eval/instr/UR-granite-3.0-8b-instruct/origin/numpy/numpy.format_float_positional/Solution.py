import numpy as np

def format_float_positional(num, ndigits=None):
    if ndigits is None:
        ndigits = int(np.ceil(np.log10(abs(num)))) + 1
    return "{:.{}f}".format(num, ndigits)
