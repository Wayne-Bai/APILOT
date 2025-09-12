from scipy.spatial.transform import Rotation
import numpy as np

# define a rotation of 45 degrees around the z-axis
theta = np.radians(45)  # convert degrees to radians
axis = [0, 0, 1]  # z-axis
rot = Rotation.from_rotvec(theta * np.array(axis))

# convert the rotation to a quaternion
quat = rot.as_quat()

print(quat)
