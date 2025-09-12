import numpy as np
from scipy.linalg import pinv

A = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
pinv_result = pinv(A)
