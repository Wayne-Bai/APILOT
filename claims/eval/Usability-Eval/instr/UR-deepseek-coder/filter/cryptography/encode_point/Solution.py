from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePublicKey
from cryptography.hazmat.primitives import serialization

def encode_ec_point_uncompressed(ec_public_key: EllipticCurvePublicKey) -> bytes:
    """
    Encodes an elliptic curve point to a byte string in uncompressed format as described in SEC 1 v2.0 section 2.3.3.

    :param ec_public_key: The elliptic curve public key to encode.
    :return: The encoded byte string in uncompressed format.
    """
    # Serialize the public key in uncompressed format
    encoded_point = ec_public_key.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.UncompressedPoint
    )
    return encoded_point
