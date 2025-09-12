import scipy.spatial.transform

# Define the quaternion
quaternion = [1, 0, 0, 0]  # Example quaternion (w, x, y, z)

# Initialize the rotation object from the quaternion
rotation = scipy.spatial.transform.Rotation.from_quat(quaternion)
