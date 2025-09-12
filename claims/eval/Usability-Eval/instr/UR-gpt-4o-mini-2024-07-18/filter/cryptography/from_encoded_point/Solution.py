from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

def decode_sec1_uncompressed(byte_string):
    if len(byte_string) < 2 or byte_string[0] != 0x04:
        raise ValueError("Invalid SEC1 uncompressed point representation.")

    # The x-coordinate is the next half of the byte_string
    half_length = (len(byte_string) - 1) // 2
    x_bytes = byte_string[1:1 + half_length]
    y_bytes = byte_string[1 + half_length:]

    # Convert x and y bytes to integers
    x = int.from_bytes(x_bytes, byteorder='big')
    y = int.from_bytes(y_bytes, byteorder='big')

    # Create an Elliptic Curve Public Numbers object
    # For demonstration, we'll use the P-256 curve
    curve = ec.SECP256R1()
    public_numbers = ec.EllipticCurvePublicNumbers(x, y, curve)

    return public_numbers

# Example usage
# byte_string = bytes.fromhex("04a5e4edddc3c2b5620ffed78558bef081d8ef69a8f3d357bca5b227c3938120c8d38d71494559b6fbff90dc386d2ef6b5373002e144dc3de1bba448a61985b")
# public_numbers = decode_sec1_uncompressed(byte_string)
# print(public_numbers)
