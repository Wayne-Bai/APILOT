from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

def decode_point(point_bytes, curve):
    """
    Decodes a byte string as described in SEC 1 v2.0 section 2.3.3 and returns an EllipticCurvePublicNumbers.
    
    Args:
        point_bytes (bytes): A byte string representing the public key.
        curve (ec.EllipticCurve): The elliptic curve associated with the public key.
    
    Returns:
        ec.EllipticCurvePublicNumbers: An EllipticCurvePublicNumbers object representing the public key.
    """
    
    # Check if the point is in uncompressed form
    if len(point_bytes)!= 1 + 2 * (curve.key_size // 8):
        raise ValueError("Invalid point length")

    if point_bytes[0]!= 4:
        raise ValueError("Point is not in uncompressed form")

    x = int.from_bytes(point_bytes[1:1 + (curve.key_size // 8)], 'big')
    y = int.from_bytes(point_bytes[1 + (curve.key_size // 8):], 'big')

    return ec.EllipticCurvePublicNumbers(x, y, curve)

# Example usage
if __name__ == "__main__":
    # Create a new elliptic curve private key
    private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
    
    # Get the public key
    public_key = private_key.public_key()
    
    # Serialize the public key in uncompressed form
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.UncompressedPoint
    )
    
    # Decode the public key
    public_numbers = decode_point(public_key_bytes, private_key.curve)
    
    print(public_numbers)
