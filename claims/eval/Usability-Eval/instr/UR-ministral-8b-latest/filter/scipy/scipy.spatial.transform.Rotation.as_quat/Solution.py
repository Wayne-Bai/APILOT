import scipy.special
import numpy as np

class Quaternion:
    def __init__(self, x=0.0, y=0.0, z=0.0, w=1.0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def normalize(self):
        norm = np.linalg.norm([self.x, self.y, self.z, self.w])
        return Quaternion(self.x / norm, self.y / norm, self.z / norm, self.w / norm)

    @staticmethod
    def conjugate(q):
        return Quaternion(q.x, -q.y, -q.z, q.w)

    @staticmethod
    def inverse(q):
        norm = np.linalg.norm([q.x, q.y, q.z, q.w]) ** 2
        return Quaternion(q.x / norm, q.y / norm, q.z / norm, q.w / norm)

    def __mul__(self, q):
        x = self.x * q.w + self.y * q.z + self.z * q.y - self.w * q.x
        y = self.w * q.x - self.x * q.z + self.z * q.w - self.y * q.x
        z = self.w * q.x - self.x * q.y + self.y * q.z - self.z * q.w
        w = self.x * q.x + self.y * q.y + self.z * q.z - self.w * q.w
        return Quaternion(x, y, z, w)

    def __rmul__(self, scalar):
        return Quaternion(self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar)

    def __repr__(self):
        return f"Quaternion({self.x}, {self.y}, {self.z}, {self.w})"
