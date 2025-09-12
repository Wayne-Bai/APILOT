from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

def encode_curve_point(curve, point):
    x = point.x.to_bytes((curve.key_size + 7) // 8, byteorder='big')
    y = point.y.to_bytes((curve.key_size + 7) // 8, byteorder='big')
    return b'\x04' + x + y

# You can use SECP256K1 curve from the cryptography library
curve = ec.SECP256K1()
private_key = ec.generate_private_key(curve)
public_key = private_key.public_key()

encoded_point = encode_curve_point(curve, public_key.public_numbers().point)
print(encoded_point)
