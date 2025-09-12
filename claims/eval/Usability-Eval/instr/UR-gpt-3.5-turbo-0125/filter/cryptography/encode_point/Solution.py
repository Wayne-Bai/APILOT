
from cryptography.hazmat.primitives.asymmetric import ec

def encode_point(point):
    if point == ec.EllipticCurvePublicKey:
        x_bytes = point.public_numbers().x.to_bytes(32, byteorder='big')
        y_bytes = point.public_numbers().y.to_bytes(32, byteorder='big')
        return b"\x04" + x_bytes + y_bytes

# Example usage
public_key = ec.generate_private_key(ec.SECP256R1()).public_key()
encoded_point = encode_point(public_key)
print(encoded_point)
