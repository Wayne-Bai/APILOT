import numpy as np
from scipy.spatial.transform import Rotation as R

# Example quaternions
quaternions = np.array([[1, 0, 0, 0],  # Identity quaternion
                        [0, 1, 0, 0],  # Example quaternion 1
                        [0, 0, 1, 0],  # Example quaternion 2
                        [0, 0, 0, 1]]) # Example quaternion 3

# Initialize Rotation object from quaternions
rotations = R.from_quat(quaternions)

# Convert rotations back to quaternions to verify
quaternions_back = rotations.as_quat()

print("Original quaternions:\n", quaternions)
print("Quaternions after conversion:\n", quaternions_back)
