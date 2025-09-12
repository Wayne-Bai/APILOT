from scipy.spatial.transform import Rotation
import numpy as np

def initialize_from_quaternion(q):
    # q is a quaternion, represented as [w, x, y, z]
    r = Rotation.from_quat(q)
    return r

# Example usage:
q = np.array([1, 0, 0, 0]) # Replace with your quaternion values
rotation = initialize_from_quaternion(q)
print(rotation.as_matrix())
