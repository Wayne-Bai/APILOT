from scipy.spatial.transform import Rotation as R

# Initialize from quaternions
rot = R.from_quat([1, 0, 0, 0])

print(rot.as_matrix())
