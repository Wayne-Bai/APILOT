from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization


def encode_ec_point_uncompressed(point: ec.EllipticCurvePublicKey) -> bytes:
    # Check if the point is on an elliptic curve
    if not isinstance(point, ec.EllipticCurvePublicKey):
        raise ValueError("Provided point is not an elliptic curve public key")

    # Get the curve parameters
    curve = point.curve
    # Get the public key as a byte string
    public_bytes = point.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )
    
    # The prefix for uncompressed points is 0x04
    prefix = bytes([0x04])
    
    # Concatenate the prefix with the public key bytes
    return prefix + public_bytes


# Example usage:
# Generate a new elliptic curve key pair
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# Encode the public key point
encoded_point = encode_ec_point_uncompressed(public_key)
print(encoded_point)
