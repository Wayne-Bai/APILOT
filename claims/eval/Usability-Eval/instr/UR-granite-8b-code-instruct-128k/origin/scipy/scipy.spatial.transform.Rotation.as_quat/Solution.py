import numpy as np
from scipy.spatial.transform import Rotation as R

# Define a rotation matrix
rotation_matrix = np.array([[0, -1, 0],
                             [1, 0, 0],
                             [0, 0, 1]])

# Convert the rotation matrix to quaternions
quaternions = R.from_matrix(rotation_matrix).as_quat()

print("Quaternions:", quaternions)
