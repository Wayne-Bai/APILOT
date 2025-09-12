import scipy.spatial.transform as transform

class Quaternion:
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_rotation_matrix(cls, R):
        return cls(*transform.Rotation.from_matrix(R).as_quat())

    @classmethod
    def from_euler_angles(cls, angles, degrees=True):
        if degrees:
            angles = [angle * (3.14159 / 180) for angle in angles]
        return cls(*transform.Rotation.from_euler('xyz', angles).as_quat())

    def __repr__(self):
        return f"Quaternion(w={self.w}, x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        return (self.w == other.w and
                self.x == other.x and
                self.y == other.y and
                self.z == other.z)

# Test the class with a rotation matrix
R = [[0, 1, 0],
     [-1, 0, 0],
     [0, 0, 1]]
q = Quaternion.from_rotation_matrix(R)
print(q)

# Test the class with euler angles
euler_angles = [45, 30, 10]
q = Quaternion.from_euler_angles(euler_angles)
print(q)
