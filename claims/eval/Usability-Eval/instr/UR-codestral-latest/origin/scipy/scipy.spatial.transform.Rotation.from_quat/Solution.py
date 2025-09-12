import numpy as np
from scipy.spatial.transform import Rotation as R

# define quaternion
q = np.array([1, 0, 0, 0]) # [scalar, i, j, k]

# create rotation object from quaternion
r = R.from_quat(q)

# convert to rotation matrix
rot_matrix = r.as_matrix()
