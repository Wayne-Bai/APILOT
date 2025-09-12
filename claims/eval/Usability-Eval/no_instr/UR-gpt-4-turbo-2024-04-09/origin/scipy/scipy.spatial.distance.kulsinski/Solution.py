# Solution 1
import numpy as np
from scipy.spatial.distance import kulsinski

x = np.array([1, 1, 0, 1], dtype=bool)
y = np.array([0, 1, 0, 1], dtype=bool)

similarity = kulsinski(x, y)
print(similarity)
