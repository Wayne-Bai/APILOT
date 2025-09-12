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
        raise ValueError("Only uncompressed points (0x04) are supported.")

    data = data[1:]
    point_size = (curve.key_size + 7) // 8

    if len(data) != 2 * point_size:
        raise ValueError("Invalid length for uncompressed point.")

    x = int.from_bytes(data[:point_size], 'big')
    y = int.from_bytes(data[point_size:], 'big')

    return EllipticCurvePublicNumbers(x, y, curve)

# Example usage:
# curve = ec.SECP256R1()
# data = b'\x04' + b'\x00' * 64  # Example uncompressed point data
# public_numbers = decode_uncompressed_point(curve, data)
# public_key = public_numbers.public_key()
