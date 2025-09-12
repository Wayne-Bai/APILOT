from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec as ecc

def encode_point(point):
    """
    Encodes an elliptic curve point to a byte string as described in SEC 1 v2.0 section 2.3.3.
    This method only supports uncompressed points.
    """
    # Convert the point to the uncompressed format
    uncompressed_point = point.to_bytes()

    # Add a 0x04 byte to the beginning of the uncompressed point
    encoded_point = b'\x04' + uncompressed_point

    return encoded_point

# Example usage
curve = ecc.SECP256R1()
point = curve.generate_private_key().public_key().public_bytes(
    encoding=ec.Encoding.UNCOMPRESSED,
    format=ec.Format.UncompressedPoint
)

encoded_point = encode_point(point)
print(encoded_point)
