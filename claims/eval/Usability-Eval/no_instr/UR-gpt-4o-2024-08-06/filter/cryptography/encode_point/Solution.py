from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def encode_ec_point(public_key):
    # Ensure the public key is an EllipticCurvePublicKey object
    if not isinstance(public_key, ec.EllipticCurvePublicKey):
        raise ValueError("The provided key is not an elliptic curve public key.")

    # Get the curve name
    curve = public_key.curve

    # Extract the x and y coordinates
    numbers = public_key.public_numbers()
    x = numbers.x
    y = numbers.y

    # Define the byte sequence to indicate uncompressed form
    uncompressed_prefix = b'\x04'

    # Calculate byte length required for coordinates
    field_byte_size = (curve.key_size + 7) // 8

    # Create byte strings for x and y coordinates, ensuring they're of correct length
    x_bytes = x.to_bytes(field_byte_size, byteorder='big')
    y_bytes = y.to_bytes(field_byte_size, byteorder='big')

    # Concatenate the prefix with the x and y coordinate bytes
    encoded_point = uncompressed_prefix + x_bytes + y_bytes

    return encoded_point

# Example usage
from cryptography.hazmat.backends import default_backend

# Generate a private key for demonstration (normally you'd be given a public key)
private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
public_key = private_key.public_key()

# Encode the public key point as a byte string
encoded_point = encode_ec_point(public_key)
print(encoded_point)
