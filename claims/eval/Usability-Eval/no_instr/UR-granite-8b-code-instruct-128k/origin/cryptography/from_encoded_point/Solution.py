from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
import binascii
def decode_byte_string(byte_string):
    decoded_point = serialization.load_der_public_key(byte_string)
    public_numbers = decoded_point.public_numbers()
    return public_numbers
