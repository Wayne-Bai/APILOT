
import numpy as np
from scipy.spatial.transform import Rotation

# Define the quaternion
quat = [0.70710678, 0, 0, 0.70710678]

# Convert quaternion to a rotation matrix
rot_matrix = Rotation.from_quat(quat).as_matrix()

print(rot_matrix)
