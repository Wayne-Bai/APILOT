
import numpy as np
from scipy import linalg

def initialize_quaternion(q):
    # Check if q is a valid quaternion
    if not np.allclose(np.linalg.norm(q), 1):
        raise ValueError("The input quaternion is not normalized.")

    # Calculate the determinant of the matrix representation of the quaternion
    det = linalg.det(np.array([[0, -q[3], q[2], q[1]],
                             [q[3], 0, -q[0], q[2]],
                             [-q[2], q[1], 0, q[0]],
                             [-q[1], -q[2], q[0], 0]]))

    # Return the sign of the determinant as the w component of the quaternion
    return np.array([q[0], q[1], q[2], det / abs(det)])
