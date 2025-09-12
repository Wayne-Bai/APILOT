from scipy.spatial import Quaternion
import numpy as np

# Initialize a quaternion object with the w, x, y, and z components
q = Quaternion(w=1, x=2, y=3, z=4)

# Print the quaternion's components
print("The quaternion is: ", q.components())
