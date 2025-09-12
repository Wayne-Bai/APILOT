from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def compress_point(point):
    coordinates = point.public_key().public_numbers().coordinates()
    x = coordinates[0].to_bytes(32, 'little')
    y = coordinates[1].to_bytes(32, 'little')
    return bytes([48 + (1 << (112 // 8 - y.x % 256))] + x + y)

def encode_point(point):
    serialized_point = point.public_key().public_numbers().public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return serialized_point

# Assuming you have an EC key pair
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

encoded_own_point = compress_point(public_key)
compressed_point = encode_point(public_key)

print(f"Encoded Own Point (uncompressed): {encoded_own_point.hex()}")
print(f"Compressed Point: {compressed_point.hex()}")
