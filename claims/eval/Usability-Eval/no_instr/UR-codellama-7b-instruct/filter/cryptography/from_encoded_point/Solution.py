
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

def decode_sec1_v2_0_uncompressed_point(byte_string):
    # Extract the header byte (0x04) from the byte string
    header_byte = byte_string[0]

    # Check if the header byte is 0x04, which indicates an uncompressed point
    if header_byte != 0x04:
        raise ValueError("Only uncompressed points are supported")

    # Extract the x-coordinate from the byte string (128 bits)
    x_coord = byte_string[1:33]

    # Convert the x-coordinate to an integer
    x_int = int.from_bytes(x_coord, "big")

    # Extract the y-coordinate from the byte string (128 bits)
    y_coord = byte_string[33:65]

    # Convert the y-coordinate to an integer
    y_int = int.from_bytes(y_coord, "big")

    # Create a new EllipticCurvePublicNumbers object from the x and y coordinates
    public_numbers = ec.EllipticCurvePublicNumbers(x_int, y_int)

    # Return the public numbers object
    return public_numbers
