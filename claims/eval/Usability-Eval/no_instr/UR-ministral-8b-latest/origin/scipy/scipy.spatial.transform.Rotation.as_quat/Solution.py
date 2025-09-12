import numpy as np
from scipy.spatial.transform import Rotation as R

def quaternion_representation(matrix):
    # Convert the given rotation matrix to a quaternion
    rotation = R.from_matrix(matrix)
    quat = rotation.as_quat()

    return quat

# Example usage:
matrix = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
quat = quaternion_representation(matrix)
print(quat)
