from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.backends import default_backend

def decode_sec1_uncompressed_point(curve, data):
    """
    Decodes a byte string in uncompressed point format for the given curve.
    Args:
    curve: An instance of EllipticCurve (from cryptography.hazmat.primitives.asymmetric.ec)
    data: byte string starting with 0x04 followed by x and y coordinates.

    Returns:
    An EllipticCurvePublicNumbers representing the public key.
    """
    if data[0] != 0x04:
        raise ValueError("Uncompressed points must start with 0x04")
    
    # Remove the first byte (0x04)
    data = data[1:]
    
    # Determine the length of a single coordinate
    coord_len = len(data) // 2
    x = int.from_bytes(data[:coord_len], byteorder='big')
    y = int.from_bytes(data[coord_len:], byteorder='big')
    
    return ec.EllipticCurvePublicNumbers(x, y, curve)

# Example usage:
curve = ec.SECP256K1()
data = bytes.fromhex("0486FAD0...")  # Put the full uncompressed point data here as a hex string

public_numbers = decode_sec1_uncompressed_point(curve, data)
public_key = public_numbers.public_key(default_backend())
print(public_key)
