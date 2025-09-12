import scipy.spatial.transform as transform

# Set up quaternion representation
my_quaternion = transform.Rotation.from_euler('xyz', [1, 2, 3], degrees=True)

# Print the quaternion
print(my_quaternion.as_quat())
