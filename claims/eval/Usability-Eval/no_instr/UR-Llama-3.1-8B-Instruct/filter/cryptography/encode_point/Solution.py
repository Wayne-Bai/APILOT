from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

def encode_point(point):
    # Convert the point to its uncompressed form
    if not point.x.verification_recoverable:
        raise ValueError("Only verification-recoverable points are supported")

    x = point.x.to_int().to_bytes(32, 'big', signed=False)
    y = point.y.to_int().to_bytes(32, 'big', signed=False)

    # Ensure the y-coordinate is even
    if y[0] % 2 == 1:
        y = bytes([0] + list(y[1:]))

    # Determine whether the y-coordinate is positive or negative
    sign = 0 if y[-1] else 1

    # Encode the point
    return bytes([4]) + x + y + sign.to_bytes(1, 'big')


def main():
    # Generate a random elliptic curve key pair
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()
    point = public_key.public_numbers().curve_point

    # Encode the point
    encoded_point = encode_point(point)

    print("Encoded point:", encoded_point)

if __name__ == "__main__":
    main()
