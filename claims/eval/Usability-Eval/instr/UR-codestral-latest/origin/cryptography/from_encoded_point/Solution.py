from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

def decode_sec1_uncompressed_point(data):
    assert data[0] == 0x04
    x = int.from_bytes(data[1:33], "big")
    y = int.from_bytes(data[33:65], "big")
    curve = ec.SECP256K1()
    return ec.EllipticCurvePublicNumbers(x, y, curve).public_key(default_backend())
