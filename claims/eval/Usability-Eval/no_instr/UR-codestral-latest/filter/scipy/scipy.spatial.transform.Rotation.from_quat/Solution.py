from scipy.spatial.transform import Rotation

# Define quaternions (qx, qy, qz, qw)
quaternions = [1, 0, 0, 0]

# Initialize the rotation from quaternions using scipy
rotation = Rotation.from_quat(quaternions)

print(rotation.as_matrix()) # print the rotation as a rotation matrix
