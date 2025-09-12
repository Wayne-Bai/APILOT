from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

def decode_public_key(public_key_bytes, curve):
    x_coordinate = int.from_bytes(public_key_bytes[1:1+(curve.key_size//8)], byteorder='big')
    y_coordinate = int.from_bytes(public_key_bytes[1+(curve.key_size//8):], byteorder='big')

    return ec.EllipticCurvePublicNumbers(x=x_coordinate, y=y_coordinate, curve=curve)

# Define the curve
curve = ec.SECP256R1()

# Here we assume that the public_key_bytes is available
public_key = decode_public_key(public_key_bytes, curve)
