from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def decode_sec1_ec_point(curve, data):
    if data[0] != 0x04:
        raise ValueError("Only uncompressed points are supported")

    # Validate the length of the data
    coord_len = (curve.key_size + 7) // 8
    if len(data) != 1 + 2 * coord_len:
        raise ValueError("Invalid data length for the specified curve")

    # Extract the coordinates
    x = int.from_bytes(data[1:1 + coord_len], byteorder="big")
    y = int.from_bytes(data[1 + coord_len:], byteorder="big")

    # Create the public numbers and return
    return ec.EllipticCurvePublicNumbers(x, y, curve)

# Example usage
def main():
    # Use P256 as an example curve
    curve = ec.SECP256R1()
    
    # This is an example of a point on the curve SECP256R1. This should be replaced with actual data.
    data = bytes.fromhex('04'
                         '6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945'
                         'd898c296'
                         '4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb64068'
                         '37bf51f5')
    
    public_numbers = decode_sec1_ec_point(curve, data)
    pub_key = public_numbers.public_key(default_backend())

    # Optional: for demonstration, let's serialize the public key
    serialized_pub_key = pub_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    print(serialized_pub_key)

if __name__ == "__main__":
    main()
