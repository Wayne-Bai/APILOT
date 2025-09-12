import numpy as np
from scipy.spatial.transform import Rotation as R

# Define the quaternion (w, x, y, z)
quat = [0.70710678, 0, 0.70710678, 0]  # Example quaternion

# Initialize the rotation object from the quaternion
rotation = R.from_quat(quat)

# Output rotation matrix
rotation_matrix = rotation.as_matrix()
print("Rotation matrix from quaternion:")
print(rotation_matrix)

# Output Euler angles (optional)
euler_angles = rotation.as_euler('xyz', degrees=True)
print("Euler angles from quaternion (in degrees):")
print(euler_angles)
