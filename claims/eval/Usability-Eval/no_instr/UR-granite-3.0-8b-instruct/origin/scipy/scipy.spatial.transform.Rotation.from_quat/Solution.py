import numpy as np
from scipy.spatial.transform import Rotation as R

# Initialize from quaternions
quat = np.array([1, 0, 0, 0])  # Example quaternion
rotation = R.from_quat(quat)
