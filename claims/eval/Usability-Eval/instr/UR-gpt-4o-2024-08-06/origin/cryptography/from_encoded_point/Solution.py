from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.backends import default_backend

def decode_point(byte_string, curve):
    """
    Decodes a byte string representing an uncompressed elliptic curve point
    and returns an EllipticCurvePublicNumbers object.
    
    :param byte_string: The byte string to decode.
    :param curve: The elliptic curve to use.
    :return: An EllipticCurvePublicNumbers object.
    """
    if len(byte_string) < 2 or byte_string[0] != 0x04:
        raise ValueError("Only uncompressed points are supported")

    # Calculate the length of the coordinate
    coordinate_length = (len(byte_string) - 1) // 2
    
    # Split the byte string into X and Y coordinates
    x_bytes = byte_string[1:1 + coordinate_length]
    y_bytes = byte_string[1 + coordinate_length:]
    
    # Convert the coordinates from bytes to integers
    x = int.from_bytes(x_bytes, byteorder='big')
    y = int.from_bytes(y_bytes, byteorder='big')
    
    # Create and return an EllipticCurvePublicNumbers object
    return ec.EllipticCurvePublicNumbers(x, y, curve)

# Example usage:
# Assuming you have byte_string as your data and you are using the SECP256R1 curve
curve = ec.SECP256R1()
byte_string = b'\x04' + b'\x9c\x3d\x9a\xbe\x2e\xda\x20\xd2\xf1\x9e\xf3\xdc\xc6\x1e\x32\xda\x47'+ \
              b'\x8f\xa6\x5e\x5e\x04\x44\xd9\x23\x07\x59\x49\x8e\x25' + \
              b'\x3f\xae\xf1\x3d\x1c\x93\x7b\xa5\xe9\x2e\xf5\xe6\x97\xe3\x2b\xd6\x26\x24' + \
              b'\xbf\x5a\xa1\x16\xd1\xfa\xfd\xee\xf1\xd5'
try:
    pub_numbers = decode_point(byte_string, curve)
    print(pub_numbers)
except ValueError as e:
    print("Error:", e)
