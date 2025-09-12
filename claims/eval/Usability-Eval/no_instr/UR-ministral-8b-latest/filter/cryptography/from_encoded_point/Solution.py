from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

def decode_ecdsa_public_point(byte_string):
    ec_point = serialization._serialization_99.load_pem_ec_public_number(byte_string)
    x, y, point_format, curve_name, is_hex = ec_point
    print(f"Curve: {curve_name}")
    print(f"Is Hex: {is_hex}")
    print(f"Point Format: {point_format}")
    print(f"X: {x}")
    print(f"Y: {y}")

# Test the function with a sample byte string for an EC Public Key
byte_string = b'\x04\xd1\x78\xcf\xa9\x28\x15\xcf\xf6\xa8\xd1\x48\x8e\xd5\x26\xc2\x54\x96\x76\xb0\xf2\xf2\xdf\x07\x42\
\x9c\x7b\x55\xea\x37\x1b\x64\x3c\xb5\x95\x1f\xc6\xc6\x98\x28\xd6\xb0\x6b\x14\x0f\x58\x28\x33\xb9\xe2...'
decode_ecdsa_public_point(byte_string)
