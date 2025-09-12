import cryptography

def decode_byte_string(byte_string):
    curve = cryptography.curves.SECP256R1()
    public_key = cryptography.keys.EllipticCurvePublicNumbers.from_encoded_point(curve, byte_string)
    return public_key
