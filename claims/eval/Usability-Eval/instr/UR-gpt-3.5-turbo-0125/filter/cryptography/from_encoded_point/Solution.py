
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat

def decode_byte_string(byte_string):
    curve = ec.SECP256R1()
    point_size = (curve.key_size + 7) // 8 * 2 + 1
    if len(byte_string) != point_size:
        raise ValueError("Invalid byte string size")

    if byte_string[0] != 4:
        raise ValueError("Invalid uncompressed point encoding")

    x = int.from_bytes(byte_string[1:33], byteorder="big")
    y = int.from_bytes(byte_string[33:], byteorder="big")

    public_numbers = ec.EllipticCurvePublicNumbers(x, y, curve)
    return public_numbers.public_key(default_backend())

# Example usage
byte_string = b'\x04...'  # Provide your byte string here
public_key = decode_byte_string(byte_string)
print(public_key.public_bytes(Encoding.X962, PublicFormat.SubjectPublicKeyInfo))
