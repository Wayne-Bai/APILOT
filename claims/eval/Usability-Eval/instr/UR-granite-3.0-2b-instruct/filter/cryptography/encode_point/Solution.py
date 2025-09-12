from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.backends import default_backend
import binascii

def ec_point_to_byte_string(point):
    if point.curve == ec.secp256r1:
        return point.point.xy().x.to_bytes(32, 'big') + point.point.xy().y.to_bytes(32, 'big')
    elif point.curve == ec.p256():
        return point.point.xy().x.to_bytes(32, 'big') + point.point.xy().y.to_bytes(32, 'big')
    else:
        raise ValueError("Unsupported curve")

# Example usage
curve = ec.SECP256R1()
point = curve.generate_key().public_point()
byte_string = ec_point_to_byte_string(point)
print(binascii.hexlify(byte_string).decode())
