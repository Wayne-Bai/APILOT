from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePublicNumbers
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

def decode_uncompressed_point(curve, data):
    """
    Decodes a byte string as described in SEC 1 v2.0 section 2.3.3 and returns an EllipticCurvePublicNumbers.
    This method only supports uncompressed points.

    :param curve: The elliptic curve to use.
    :param data: The byte string to decode.
    :return: EllipticCurvePublicNumbers
    """
    if data[0] != 0x04:
        raise ValueError("Only uncompressed points (starting with 0x04) are supported.")

    data = data[1:]  # Remove the uncompressed point indicator
    point_length = len(data) // 2

    x = int.from_bytes(data[:point_length], 'big')
    y = int.from_bytes(data[point_length:], 'big')

    return EllipticCurvePublicNumbers(x, y, curve)

# Example usage:
# curve = ec.SECP256R1()
# data = b'\x04' + b'\x00' * 64  # Example uncompressed point data
# public_numbers = decode_uncompressed_point(curve, data)
# public_key = public_numbers.public_key()
