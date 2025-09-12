import numpy as np
from scipy.spatial.transform import Rotation as R

# Quaternion representation
quaternion = R.from_quat([0.5, 0.5, 0.5, 0.5])
print("Quaternion:", quaternion.as_quat())
