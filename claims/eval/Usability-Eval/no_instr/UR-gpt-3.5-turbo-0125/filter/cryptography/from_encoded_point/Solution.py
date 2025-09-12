
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

def decode_byte_string(byte_string):
    curve = ec.SECP256R1()
    curve_public_numbers = curve.decode_point(byte_string)
    return ec.EllipticCurvePublicNumbers(curve.curve, curve_public_numbers).public_key(default_backend())
