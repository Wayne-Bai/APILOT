from scipy.spatial.transform import Rotation as R

# Define a rotation matrix
rotation_matrix = [[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1]]

# Create a Rotation object
rotation = R.from_matrix(rotation_matrix)

# Represent the rotation as quaternions
quaternion = rotation.as_quat()

print("Quaternions:", quaternion)
