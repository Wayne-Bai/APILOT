import numpy as np
from scipy.spatial.transform import Rotation

# Define a rotation
rotation = Rotation.from_euler('xyz', np.array([10, 20, 30]), degrees=True)

# Convert to quaternion
quaternion = rotation.as_quat()

print(f'The representation as a quaternion is: {quaternion}')
