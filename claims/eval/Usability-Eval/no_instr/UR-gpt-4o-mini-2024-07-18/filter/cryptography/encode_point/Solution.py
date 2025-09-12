from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def encode_uncompressed_curve_point(point: ec.EllipticCurvePublicKey) -> bytes:
    if not isinstance(point, ec.EllipticCurvePublicKey):
        raise ValueError("Input must be an instance of EllipticCurvePublicKey.")
    
    # Get the encoded point in uncompressed format
    encoded_point = point.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.UncompressedPoint
    )
    return encoded_point

# Example usage: Generate a key and encode the public key point
private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
public_key = private_key.public_key()

encoded_point = encode_uncompressed_curve_point(public_key)
print(encoded_point.hex())
