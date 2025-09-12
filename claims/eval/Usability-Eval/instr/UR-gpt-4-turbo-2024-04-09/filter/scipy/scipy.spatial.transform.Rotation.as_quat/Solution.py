import scipy.spatial.transform

# Example quaternion (w, x, y, z)
q = scipy.spatial.transform.Rotation.from_quat([0.5, 0.5, 0.5, 0.5])

print("Quaternion representation:", q.as_quat())
