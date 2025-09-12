from cryptography.hazmat.primitives.asymmetric import ec

def encode_ec_point_to_bytes(point: ec.EllipticCurvePublicKey) -> bytes:
    # Obtain the x and y coordinates of the elliptic curve point
    numbers = point.public_numbers()
    x = numbers.x.to_bytes((numbers.x.bit_length() + 7) // 8, byteorder='big')
    y = numbers.y.to_bytes((numbers.y.bit_length() + 7) // 8, byteorder='big')
    
    # Concatenate the result with the uncompressed point indicator byte
    return b'\x04' + x + y

# Example usage
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

encoded_point = encode_ec_point_to_bytes(public_key)
print(encoded_point.hex())
