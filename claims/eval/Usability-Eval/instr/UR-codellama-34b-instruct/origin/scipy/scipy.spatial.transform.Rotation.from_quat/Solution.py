import numpy as np
from scipy.spatial import Rotation

# Define the quaternion
q = np.array([0.5, 0.2, -0.3, 0.7])

# Initialize the rotation matrix from the quaternion
R = Rotation.from_quat(q)
