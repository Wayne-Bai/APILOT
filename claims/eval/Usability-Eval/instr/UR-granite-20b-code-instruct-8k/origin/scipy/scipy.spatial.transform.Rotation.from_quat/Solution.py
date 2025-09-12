from scipy.spatial.transform import Rotation

# Define a set of quaternions
quaternions = [
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0]
]

# Initialize a Rotation object from the quaternions
rotation = Rotation.from_quaternions(quaternions)

# Print the resulting rotation matrix
print(rotation.as_matrix())
