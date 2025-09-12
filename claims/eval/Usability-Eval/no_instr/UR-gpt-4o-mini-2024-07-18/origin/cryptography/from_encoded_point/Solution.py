from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def decode_sec1_uncompressed(byte_string):
    if len(byte_string) < 2 or byte_string[0] != 0x04:
        raise ValueError("Invalid uncompressed point format.")
    
    # Extract the x and y coordinates from the byte string
    half_length = (len(byte_string) - 1) // 2
    x_bytes = byte_string[1:1 + half_length]
    y_bytes = byte_string[1 + half_length:]

    # Create EllipticCurvePublicNumbers using x and y
    x = int.from_bytes(x_bytes, byteorder='big')
    y = int.from_bytes(y_bytes, byteorder='big')
    curve = ec.SECP256R1()  # You can change it to the appropriate curve as needed

    return ec.EllipticCurvePublicNumbers(x, y, curve)
