from scipy.spatial.transform import Rotation as R

# Define a rotation using quaternions
rotation = R.from_quat([0.5, 0.5, 0.5, 0.5])

# Print the rotation matrix
print(rotation.as_matrix())
