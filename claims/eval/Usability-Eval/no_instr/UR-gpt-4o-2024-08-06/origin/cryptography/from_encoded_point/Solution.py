from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def decode_ec_point(data, curve):
    """
    Decode an elliptic curve point from a byte string as per SEC 1 v2.0 section 2.3.3.
    
    :param data: Byte string representing the elliptic curve point.
    :param curve: The elliptic curve object (e.g., ec.SECP256R1()).
    
    :return: EllipticCurvePublicNumbers object.
    """
    # Check if the point is uncompressed (starts with 0x04)
    if data[0] != 0x04:
        raise ValueError("Only uncompressed points are supported")

    # Calculate the size of each coordinate
    coordinate_size = (len(data) - 1) // 2

    # Extract x and y coordinates from the data
    x = int.from_bytes(data[1:1 + coordinate_size], byteorder='big')
    y = int.from_bytes(data[1 + coordinate_size:], byteorder='big')

    # Create an EllipticCurvePublicNumbers object
    ec_public_numbers = ec.EllipticCurvePublicNumbers(x, y, curve)

    return ec_public_numbers

# Example usage with a sample uncompressed point on the SECP256R1 curve
curve = ec.SECP256R1()
uncompressed_point = bytes.fromhex(
    '04'  # Indicates uncompressed point
    '6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296'  # x-coordinate
    '4fe342e2fe1a7f9b8ee7eb4a7c0f9e162cbf4e1b8e0731568e4e3daaa4ea7ed2'  # y-coordinate
)
public_numbers = decode_ec_point(uncompressed_point, curve)

# Output the public numbers
print(public_numbers)
# Optionally, convert to a public key
public_key = public_numbers.public_key()
print(public_key)
