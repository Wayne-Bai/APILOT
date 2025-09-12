import numpy as np
from scipy.spatial.transform import Rotation as R

# Example quaternion (w, x, y, z)
quaternion = [0.7071, 0.0, 0.7071, 0.0]

# Initialize rotation from the quaternion
rotation = R.from_quat(quaternion)

# To get the rotation matrix
rotation_matrix = rotation.as_matrix()

# To get the Euler angles from the rotation
euler_angles = rotation.as_euler('xyz', degrees=True)

print("Rotation Matrix:\n", rotation_matrix)
print("Euler Angles (degrees):", euler_angles)
