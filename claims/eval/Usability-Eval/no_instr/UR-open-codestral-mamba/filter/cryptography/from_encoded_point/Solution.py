from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

def decrypt_byte_string(byte_string):
    public_numbers = serialization.load_der_public_key(byte_string).public_numbers()
    ec_public_numbers = ec.EllipticCurvePublicNumbers(public_numbers.x, public_numbers.y, ec.SECP256R1())
    return ec_public_numbers
