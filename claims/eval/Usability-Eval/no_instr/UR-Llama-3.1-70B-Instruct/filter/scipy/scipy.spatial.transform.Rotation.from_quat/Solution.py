import numpy as np
from scipy.spatial.transform import Rotation as R

def initialize_from_quaternions(quaternions):
    """
    Initialize rotation objects from quaternions.

    Parameters:
    quaternions (array_like, shape (..., 4)): Quaternions with elements in the form of [x, y, z, w] where w is the scalar form.

    Returns:
    Rotation instance containing rotations represented by the input quaternions.
    """
    # Convert quaternions to a numpy array
    quaternions = np.asarray(quaternions)
    
    # Initialize Rotation object from quaternions
    rotation_object = R.from_quat(quaternions)
    
    return rotation_object

# Example usage:
quaternions = [[0.70710678, 0.70710678, 0, 0], [0, 0, 0.70710678, 0.70710678]]  # w (real part) is the last element
rotation_object = initialize_from_quaternions(quaternions)
print(rotation_object)
