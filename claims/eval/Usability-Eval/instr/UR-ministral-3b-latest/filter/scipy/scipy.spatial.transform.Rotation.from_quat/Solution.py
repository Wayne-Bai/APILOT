from scipy.spatial.transform import Rotation as R

# Example usage
r = R.from_quat([1, 0, 0, 0])  # Creates a rotation from a quaternion
print(r.as_euler('xyz'))
