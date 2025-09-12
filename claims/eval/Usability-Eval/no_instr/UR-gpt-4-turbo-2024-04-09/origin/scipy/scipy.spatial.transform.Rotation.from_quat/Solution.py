import scipy.spatial.transform

# Example quaternion: can be any normalized real numbers (q0, q1, q2, q3)
q = [1, 0, 0, 0]  # this is the identity quaternion

# Initializing from quaternions using Rotation from scipy.spatial.transform
rotation = scipy.spatial.transform.Rotation.from_quat(q)

print(rotation.as_matrix())  # Output the rotation matrix corresponding to the quaternion
