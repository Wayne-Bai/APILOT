import numpy as np
from scipy.spatial.transform import Rotation as R

# Function to convert Euler angles to quaternions
def euler_to_quaternion(angles):
    # Create a Rotation object from Euler angles (roll, pitch, yaw)
    rotation = R.from_euler('xyz', angles, degrees=True)
    # Convert the Rotation object to quaternion
    quaternion = rotation.as_quat()
    return quaternion

# Example usage
angles = [30, 45, 60]  # Example Euler angles in degrees
quaternion = euler_to_quaternion(angles)
print("Quaternion representation:", quaternion)
