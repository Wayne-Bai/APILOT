import scipy.spatial.transform as transform
import numpy as np

def euler_to_quaternion(euler_angles):
    """
    Convert Euler angles to quaternion.
    
    Parameters:
    euler_angles (list): Euler angles in radians in the format [roll, pitch, yaw].
    
    Returns:
    quaternion (list): Quaternion in the format [w, x, y, z].
    """
    roll, pitch, yaw = euler_angles
    quat = transform.Rotation.from_euler('xyz', [roll, pitch, yaw]).as_quat()
    return quat.tolist()

def quaternion_to_euler(quaternion):
    """
    Convert quaternion to Euler angles.
    
    Parameters:
    quaternion (list): Quaternion in the format [w, x, y, z].
    
    Returns:
    euler_angles (list): Euler angles in radians in the format [roll, pitch, yaw].
    """
    quat = transform.Rotation.from_quat(quaternion)
    euler_angles = quat.as_euler('xyz', degrees=False)
    return euler_angles.tolist()

# Test the functions
euler_angles = [np.radians(45), np.radians(30), np.radians(10)]
quaternion = euler_to_quaternion(euler_angles)
print(f'Euler angles: {euler_angles}')
print(f'Quaternion: {quaternion}')

quaternion_from_euler = [0.92387953251129, -0.244024054502773, -0.153305484115388, 0.202642644177739]
euler_angles_from_quaternion = quaternion_to_euler(quaternion_from_euler)
print(f'Quaternion: {quaternion_from_euler}')
print(f'Euler angles from quaternion: {euler_angles_from_quaternion}')
