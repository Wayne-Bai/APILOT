import numpy as np
from scipy.spatial.transform import Rotation as R

# Example quaternion (w, x, y, z)
quaternion = [1, 0, 0, 0]  # Replace with your quaternion values

# Initialize a rotation from the quaternion
rotation = R.from_quat(quaternion)

# Example of converting it to rotation matrix
rotation_matrix = rotation.as_matrix()

# Print the rotation matrix
print(rotation_matrix)
