from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def encode_point(x: int, y: int) -> bytes:
    point = ec.EllipticCurvePublicKey.from_encoded_point(
        ec.SECP256K1(),
        b''.join([int.to_bytes(32, 'big', signed=False) for int in [x, y]])
    )
    return point.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.UncompressedPoint,
    )

# Usage example
x = 12345
y = 67890
print(encode_point(x, y))
