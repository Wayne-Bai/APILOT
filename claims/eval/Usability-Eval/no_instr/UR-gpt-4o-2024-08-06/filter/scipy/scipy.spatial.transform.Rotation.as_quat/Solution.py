import numpy as np
from scipy.spatial.transform import Rotation as R

# Example: converting Euler angles to quaternions
# Define Euler angles: yaw, pitch, roll in radians
yaw = np.pi / 4    # 45 degrees
pitch = np.pi / 6  # 30 degrees
roll = np.pi / 3   # 60 degrees

# Create a rotation object from Euler angles
rotation = R.from_euler('zyx', [yaw, pitch, roll])

# Convert rotation to quaternions
quaternion = rotation.as_quat()

print("Quaternion representation:", quaternion)
