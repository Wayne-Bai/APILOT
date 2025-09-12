from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

# Define the elliptic curve parameters (P-256 in this case)
curve = ec.SEC_p256r1()

# Define the byte string to hold the encoded point
encoded_point = b''

# Encode the x coordinate of the point
encoded_point += struct.pack('>I', curve.elliptic_curve.field_group.modulus)
encoded_point += struct.pack('>I', curve.elliptic_curve.field_group.order)
encoded_point += b'\x04' + struct.pack('>I', curve.elliptic_curve.base_point.y)

# Encode the y coordinate of the point
encoded_point += struct.pack('>I', curve.elliptic_curve.base_point.x)

print(encoded_point)
