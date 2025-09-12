
import numpy as np

# Define quaternion representation
class Quaternion:
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    # Method to return quaternion as a numpy array
    def as_array(self):
        return np.array([self.w, self.x, self.y, self.z])

# Example quaternion
quat = Quaternion(1, 2, 3, 4)
print(quat.as_array())
