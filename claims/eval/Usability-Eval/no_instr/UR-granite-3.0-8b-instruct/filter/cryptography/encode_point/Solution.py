from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import utils

def encode_point(point):
    if point.affine():
        return point.to_bytes(ec.SECP256R1().curve_order, 'big')
    else:
        raise ValueError("Point must be affine")

# Example usage:
curve = ec.SECP256R1()
point = ec.EllipticCurvePoint(curve, 1, 2)  # Replace with your point
encoded_point = encode_point(point)
print(encoded_point.hex())
