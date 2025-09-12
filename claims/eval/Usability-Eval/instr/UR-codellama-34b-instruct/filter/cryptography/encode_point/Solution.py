
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidPointError

def encode_point(x, y):
    curve = ec.SECP256R1()
    point = ec.EllipticCurvePublicKey(curve=curve, x=x, y=y)
    try:
        encoded = point.encode('byte')
        return encoded
    except InvalidPointError as e:
        raise ValueError("Invalid point coordinates") from e
