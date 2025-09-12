from scipy.spatial.transform import Rotation as R

# Example Euler angles in radians (for example: roll, pitch, yaw)
euler_angles = [0.1, 0.2, 0.3]

# Create a Rotation object from Euler angles
rotation = R.from_euler('xyz', euler_angles)

# Convert the rotation to a quaternion
quaternion = rotation.as_quat()

print("Quaternion representation:", quaternion)
