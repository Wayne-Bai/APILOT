import cryptography.hazmat.primitives.asymmetric.utils as utils
from cryptography.exceptions import InvalidTagException

def decode_ecdsa_point(data):
    """Decodes a byte string as described in SEC 1 v2.0 section 2.3.3 and returns an EllipticCurvePublicNumbers."""
    try:
        point = utils.decode_dss_signature(data)
        return EllipticCurvePublicNumbers(point[0], point[1])
    except InvalidTagException:
        raise ValueError("Invalid DSS signature")
