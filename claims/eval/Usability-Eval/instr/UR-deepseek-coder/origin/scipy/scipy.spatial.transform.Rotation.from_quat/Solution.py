import numpy as np
from scipy.spatial.transform import Rotation as R

# Example quaternion (w, x, y, z)
quaternion = [0.7071, 0.0, 0.7071, 0.0]

# Initialize rotation from quaternion
rotation = R.from_quat(quaternion)

# Convert rotation to other representations if needed
rotation_matrix = rotation.as_matrix()
euler_angles = rotation.as_euler('xyz', degrees=True)

print("Rotation Matrix:")
print(rotation_matrix)
print("\nEuler Angles (degrees):")
print(euler_angles)
