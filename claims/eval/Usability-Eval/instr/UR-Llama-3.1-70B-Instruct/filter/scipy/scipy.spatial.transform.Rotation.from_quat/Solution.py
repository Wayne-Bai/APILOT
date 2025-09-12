import scipy.spatial.transform as transform

def initialize_from_quaternion():
    # Define quaternions
    q1 = transform.Rotation.from_quat([0.707106781, 0.707106781, 0, 0])
    q2 = transform.Rotation.from_quat([0, 0, 0, 1])

    # Apply rotations
    q1_inv = q1.inv()
    q3 = q1_inv * q2

    print("Quaternion 1: ", q1.as_quat())
    print("Quaternion 2: ", q2.as_quat())
    print("Quaternion 3 (q1_inv * q2): ", q3.as_quat())

# Run the function
initialize_from_quaternion()
