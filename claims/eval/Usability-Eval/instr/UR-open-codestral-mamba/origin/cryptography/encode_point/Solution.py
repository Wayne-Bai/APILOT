from cryptography.hazmat.primitives.asymmetric.utils import encode_dss_signature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

def point_to_bytes(point, curve):
    # Encode the point as bytes
    return point.public_bytes(
        encoding=ec.EllipticCurvePublicKeyFormat.UncompressedPoint,
        compression=ec.EllipticCurvePublicKeyCompression.UncompressedPoint,
        format=ec.EllipticCurvePublicNumbersFormat.Raw,
        curve=curve
    )

# Example usage
curve = ec.SECP256R1()
private_key = ec.generate_private_key(curve)
public_key = private_key.public_key()
point = public_key.public_numbers()

encoded_point = point_to_bytes(public_key, curve)
print(encoded_point)
