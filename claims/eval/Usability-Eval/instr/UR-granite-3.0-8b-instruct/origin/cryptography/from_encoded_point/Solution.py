from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def decode_public_key(public_key_bytes):
    public_key = serialization.load_der_public_key(public_key_bytes, ec.SECP256R1())
    return public_key.public_numbers()
