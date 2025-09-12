
from scipy.spatial.transform import Rotation

# Create a quaternion representation
quat = Rotation.from_euler('xyz', [0, 0, 0]).as_quat()
print("Quaternion representation:", quat)
