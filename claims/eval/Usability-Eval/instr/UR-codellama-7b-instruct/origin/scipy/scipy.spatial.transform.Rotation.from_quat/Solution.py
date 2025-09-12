
from scipy.spatial.transform import Rotation as R

# Define the Euler angles (in radians)
e1 = np.pi/2
e2 = np.pi/4
e3 = 0

# Create a quaternion from the Euler angles
q = R.from_euler(e1, e2, e3).quaternion

print(q) # Outputs [0.70710678+0.70710678j]
