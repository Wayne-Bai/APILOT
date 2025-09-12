from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def decode_point(point_bytes):
    # Uncompress the point
    point = ec.Point.uncompressed_decoder(point_bytes)

    # Convert the point to EllipticCurvePublicNumbers
    public_numbers = ec.EllipticCurvePublicNumbers.from_public_key(point)

    return public_numbers
