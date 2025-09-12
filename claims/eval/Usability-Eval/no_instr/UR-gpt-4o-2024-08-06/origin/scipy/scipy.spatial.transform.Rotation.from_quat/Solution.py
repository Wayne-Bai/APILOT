import scipy.spatial.transform

# Define a quaternion as [x, y, z, w]
quaternion = [0.0, 0.0, 0.0, 1.0]

# Initialize a Rotation object from the quaternion
rotation = scipy.spatial.transform.Rotation.from_quat(quaternion)

# Output the rotation matrix
rotation_matrix = rotation.as_matrix()
print("Rotation Matrix from Quaternion:")
print(rotation_matrix)

# Output the Euler angles
euler_angles = rotation.as_euler('xyz', degrees=True)
print("Euler Angles from Quaternion (in degrees):")
print(euler_angles)
