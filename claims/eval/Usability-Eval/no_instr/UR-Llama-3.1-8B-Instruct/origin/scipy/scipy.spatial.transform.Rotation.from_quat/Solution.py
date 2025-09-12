import numpy as np
from scipy.spatial.transform import Rotation as R

# Define a quaternion
quaternion = np.array([0.5, 0.3, 0.2, 0.1])

# Convert the quaternion to a rotation matrix
rotation_matrix = R.from_quat(quaternion).as_matrix()

# Print the rotation matrix
print(rotation_matrix)
