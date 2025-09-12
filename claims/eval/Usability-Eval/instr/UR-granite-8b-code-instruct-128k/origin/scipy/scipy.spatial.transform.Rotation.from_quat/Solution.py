from scipy.spatial.transform import Rotation as R
import numpy as np

# Create a random quaternion
q = np.random.rand(4)
q /= np.linalg.norm(q)

# Initialize a rotation object from the quaternion
r = R.from_quat(q)

# Print the rotation matrix
print(r.as_matrix())
