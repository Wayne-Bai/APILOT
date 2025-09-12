from scipy.spatial.transform import Rotation as R
import numpy as np

# Define a quaternion
q = np.array([0.707, 0.707, 0.0, 0.0])

# Initialize a rotation object from the quaternion
r = R.from_quat(q)

# Get the rotation matrix
rot_mat = r.as_matrix()

# Get the Euler angles
euler_angles = r.as_euler('XYZ', degrees=True)

# Print the results
print("Rotation matrix:")
print(rot_mat)
print("Euler angles (XYZ):")
print(euler_angles)
