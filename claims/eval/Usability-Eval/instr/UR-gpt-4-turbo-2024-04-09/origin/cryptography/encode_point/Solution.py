from cryptography.hazmat.primitives.asymmetric import ec

def encode_elliptic_curve_point(point):
    """
    Encodes an elliptic curve point to a byte string as described in SEC 1 v2.0 section 2.3.3.
    This function only supports uncompressed points.

    Args:
    point (ec.EllipticCurvePublicKey): The elliptic curve public key object.

    Returns:
    bytes: The uncompressed point encoded as a byte string.
    """
    x = point.public_numbers().x
    y = point.public_numbers().y
    curve = point.curve
    byte_len = (curve.key_size + 7) // 8  # calculate the byte length for the coordinates

    # Format the point as: 0x04 || x || y
    return bytes([4]) + x.to_bytes(byte_len, 'big') + y.to_bytes(byte_len, 'big')

# Example usage:
# Generate an elliptic curve key pair
private_key = ec.generate_private_key(ec.SECP256K1())
public_key = private_key.public_key()

# Encode the public key point
encoded_point = encode_elliptic_curve_point(public_key)
print("Encoded point:", encoded_point.hex())
