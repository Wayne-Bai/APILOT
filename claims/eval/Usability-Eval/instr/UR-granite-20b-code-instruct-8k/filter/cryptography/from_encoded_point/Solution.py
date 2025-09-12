from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def decode_point(byte_string):
    """
    Decodes a byte string as described in SEC 1 v2.0 section 2.3.3 and
    returns an EllipticCurvePublicNumbers.

    Only supports uncompressed points.
    """
    backend = default_backend()
    point = serialization.load_pem_public_key(
        byte_string,
        backend=backend
    )

    return point.public_numbers()
