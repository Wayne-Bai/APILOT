from cryptography.hazmat.primitives.asn1 import encode
from cryptography.hazmat.primitives.asn1 import oaeppadding
from cryptography.hazmat.primitives.asn1 import x509
from cryptography.hazmat.primitives.asn1 import serialize
from cryptography.hazmat.primitives import hashes, serialization

# Import necessary classes for elliptic curve cryptography
from cryptography.hazmat.primitives import ec
from cryptography.hazmat.backends import default_backend

def encode_elliptic_curve_point(point):
    # Ensure the point is an uncompressed point
    if point.y() == 0:
        raise ValueError("Point must be uncompressed ( SEC 1 v2.0, section 2.3.3 )")

    backend = default_backend()
    # Serialize the point using the uncompressed format
    uncompressed_point = bytes([74]) + point.Q.x().to_bytes(32, 'big') + point.Q.y().to_bytes(32, 'big')
    return uncompressed_point

# Example usage:
# Generate a private key and corresponding public key
private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
public_key = private_key.public_key()

# Generate a random uncompressed point
point = ec.derive_public_key(private_key, b'random_derivation_data'.encode(), backend=default_backend())

# Encode the point
encoded_point = encode_elliptic_curve_point(point)

print(encoded_point.hex())
