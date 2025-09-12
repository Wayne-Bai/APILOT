from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
import os
import math

def encode_point(point):
    """
    Encodes an elliptic curve point to a byte string as described in SEC 1 v2.0 section 2.3.3.
    This method only supports uncompressed points.

    Parameters:
    point (cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePublicKey): 
        The elliptic curve point to be encoded.

    Returns:
    bytes: The encoded elliptic curve point.
    """

    # Get the public bytes of the point using the uncompressed point encoding
    public_bytes = point.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.UncompressedPoint
    )

    return public_bytes


# Example usage of the function
def main():
    # Generate a new private key
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())

    # Get the public key
    public_key = private_key.public_key()

    # Encode the public key point
    encoded_point = encode_point(public_key)

    print("Encoded point:", encoded_point)


if __name__ == "__main__":
    main()
