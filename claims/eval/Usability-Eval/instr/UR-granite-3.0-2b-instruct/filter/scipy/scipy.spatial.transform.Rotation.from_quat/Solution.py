from scipy.spatial.transform import Rotation as R

# Initialize a rotation object from quaternions
r = R.from_quat([1, 0, 0, 0])

# Print the rotation matrix
print(r.matrix)
