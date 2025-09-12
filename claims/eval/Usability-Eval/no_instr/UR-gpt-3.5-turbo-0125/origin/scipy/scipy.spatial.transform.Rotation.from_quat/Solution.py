
from scipy.spatial.transform import Rotation

# Initialize from quaternions
quaternion = [0.5, 0.5, 0.5, 0.5]
r = Rotation.from_quat(quaternion)
print(r.as_matrix())
