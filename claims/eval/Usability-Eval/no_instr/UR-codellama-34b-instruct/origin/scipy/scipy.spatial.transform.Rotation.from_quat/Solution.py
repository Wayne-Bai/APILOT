import numpy as np
from scipy.spatial.transform import Rotation

# Define the quaternion components
q0 = 1.0
q1 = 2.0
q2 = 3.0
q3 = 4.0

# Create a rotation object from the quaternion
rot = Rotation.from_quat(np.array([q0, q1, q2, q3]))
