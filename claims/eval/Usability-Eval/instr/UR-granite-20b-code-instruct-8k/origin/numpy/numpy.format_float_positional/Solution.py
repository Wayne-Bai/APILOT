import numpy as np

def format_float_positional(number, precision=2):
    return format(round(number, precision), f'.{precision}f')
