from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

def decode_public_key(byte_string):
    # Load the public key from the byte string
    public_key = serialization.load_balanced_bytes(byte_string, default_backend())

    # Ensure the public key is an instance of EllipticCurvePublicKey
    if not isinstance(public_key, ec.EllipticCurvePublicKey):
        raise ValueError("Provided byte string does not represent a valid uncompressed public key")

    # Get the elliptic curve parameters
    curve = public_key.public_numbers().curve

    # Return the EllipticCurvePublicNumbers
    return ec.EllipticCurvePublicNumbers(
        public_key.public_numbers().x,
        public_key.public_numbers().y,
        curve
    )
