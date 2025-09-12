import scipy
from scipy.spatial.distance import kulsinski

array1 = np.array([True, False, True, False])
array2 = np.array([False, True, False, True])

dissimilarity = kulsinski(array1, array2)
print(dissimilarity)
