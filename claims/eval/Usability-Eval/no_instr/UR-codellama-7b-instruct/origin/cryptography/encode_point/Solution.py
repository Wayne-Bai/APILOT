
import cryptography
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

def encode_elliptic_curve_point(point: ec.EllipticCurvePoint, encoding: str) -> bytes:
    if encoding not in ["uncompressed"]:
        raise ValueError("Unsupported encoding")
    return point.serialize_compressed()
