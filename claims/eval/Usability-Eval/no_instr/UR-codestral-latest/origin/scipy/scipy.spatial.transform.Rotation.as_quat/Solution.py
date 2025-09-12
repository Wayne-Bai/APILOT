# Importing required module
from scipy.spatial.transform import Rotation as R

# Define some rotation as a matrix or axis-angle representation
# Here, I use a rotation of 90 degrees around the x-axis as an example
rotation = R.from_rotvec(90 * np.array([1, 0, 0]))

# Convert the rotation to a quaternion
quaternion = rotation.as_quat()

print("Quaternion representation of the rotation:", quaternion)
