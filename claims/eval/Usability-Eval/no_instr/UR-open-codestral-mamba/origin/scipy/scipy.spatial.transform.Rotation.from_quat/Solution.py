import numpy as np
from scipy.spatial.transform import Rotation as R

# Create a quaternion
q = R.from_quat([1, 0, 0, 0])  # Example quaternion, replace with your values

# Initialize from quaternion
initializer = R.from_quat(q.as_quat())

print(initializer.as_matrix())  # Prints the rotation matrix
