import numpy as np
from scipy.spatial.transform import Rotation as R

# Define a function to initialize from quaternions
def from_quaternions(quat):
    """
    Initialize Rotation object from quaternions.

    Parameters
    ----------
    quat : array_like
        Quaternions in the format [w, x, y, z].

    Returns
    -------
    Rotation object
        The rotation applied by the quaternions.
    """
    return R.from_quat(quat)

# Define a quaternion
quat = np.array([0.1, 0.2, 0.3, 0.4])

# Initialize rotation from quaternion
rotation = from_quaternions(quat)

# Print the rotation matrix
print(rotation.as_matrix())
