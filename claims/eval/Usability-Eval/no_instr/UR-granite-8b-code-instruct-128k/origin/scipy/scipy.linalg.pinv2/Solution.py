import scipy
import scipy.linalg
def pseudo_inverse(matrix):
 return scipy.linalg.pinv(matrix)
