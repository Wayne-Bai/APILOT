import numpy as np
from scipy.spatial.transform import Rotation as R

# Define a quaternion
quaternion = np.array([1, 0, 0, 0])

# Convert the quaternion to a rotation matrix
rotation_matrix = R.from_quat(quaternion).as_matrix()

print(rotation_matrix)
