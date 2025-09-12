import numpy as np
from scipy.spatial.transform import Rotation as R

# Example rotation matrix (3x3)
rotation_matrix = np.array([
    [0, -1, 0],
    [1, 0, 0],
    [0, 0, 1]
])

# Create a Rotation object from the rotation matrix
rotation = R.from_matrix(rotation_matrix)

# Convert the rotation to a quaternion
quaternion = rotation.as_quat()

print("Quaternion representation:", quaternion)
