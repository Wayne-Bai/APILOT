from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

def encode_uncompressed_point(public_key):
    """
    Encodes an elliptic curve public key to an uncompressed byte string.
    
    Args:
    - public_key (EllipticCurvePublicKey): The public key to encode.
    
    Returns:
    - bytes: The uncompressed point as a byte string.
    """
    # Encoding the public key to an uncompressed point byte string
    uncompressed_point = public_key.public_bytes(
        encoding=Encoding.X962, 
        format=PublicFormat.UncompressedPoint
    )
    return uncompressed_point

# Example usage
# Generate an EC key pair
private_key = ec.generate_private_key(ec.SECP256K1())  # Using SECP256K1 curve, can use any other supported curve
public_key = private_key.public_key()

# Get the uncompressed byte string of the public key
uncompressed_byte_string = encode_uncompressed_point(public_key)
print(uncompressed_byte_string)
