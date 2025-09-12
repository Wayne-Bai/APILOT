import numpy as np
from scipy.spatial.transform import Rotation as R

# Function to convert Euler angles to quaternion
def euler_to_quaternion(roll, pitch, yaw):
    # Create a rotation object from Euler angles (in radians)
    r = R.from_euler('xyz', [roll, pitch, yaw])
    # Convert to quaternion
    quaternion = r.as_quat()  # returns [x, y, z, w]
    return quaternion

# Example usage
roll = np.radians(30)  # Convert degrees to radians
pitch = np.radians(45)
yaw = np.radians(60)

quaternion = euler_to_quaternion(roll, pitch, yaw)
print("Quaternion:", quaternion)
