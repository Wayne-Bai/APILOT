from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature, ValueError

def decode_point( elliptic_curve, byte_string):
    # Get the expected size for the given curve
    expected_size = elliptic_curve.key_size // 8
    
    # Ensure that the byte string is of the correct size
    if len(byte_string)!= expected_size * 2 + 1:
        raise ValueError("Invalid compressed point size")

    # Decompress the point
    if byte_string[0] == 0x04:  # Uncompressed
        # Initialize x and y values
        x = int.from_bytes(byte_string[1:expected_size + 1], byteorder='big')
        y = int.from_bytes(byte_string[expected_size + 1:], byteorder='big')
    else:
        raise ValueError("Only uncompressed points are supported")

    # Generate EllipticCurvePublicNumbers
    public_numbers = ec.EllipticCurvePublicNumbers(x, y, elliptic_curve)
    
    return public_numbers


def load_curve_public_numbers( elliptic_curve_name, byte_string):
    # Acquire the curve
    elliptic_curve = ec.get_curve_for_name(getattr(ec, elliptic_curve_name))
    public_numbers = decode_point(elliptic_curve, byte_string)

    return public_numbers


# Usage example
# Specify the curve name (e.g., 'SECP256R1')
curve_name = 'SECP256R1'
curve = ec.get_curve_for_name(getattr(ec, curve_name))


# Create the private key for the given curve
private_key = ec.generate_private_key(curve)


# Get the corresponding public key
public_key = private_key.public_key()


# Serialize the public key
public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.X962,
    format=serialization.PublicFormat.UncompressedPoint
)


# Decode the given public key bytes
public_numbers = load_curve_public_numbers(curve_name, public_bytes)


# Log the Public Numbers object
print("Public Numbers: ", public_numbers)

# Print public numbers in detail 
print(public_numbers.public_key(default_backend()).public_bytes(
    encoding=serialization.Encoding.X962,
    format=serialization.PublicFormat.UncompressedPoint
))
