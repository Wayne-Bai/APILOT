import numpy as np

try:
    np.empty((3, 4, 5)).sum(axis=3)
except np.AxisError as e:
    print(f"AxisError: {e}")
