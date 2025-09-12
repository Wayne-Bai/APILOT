from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

def encode_point(point):
    """
    Encodes an elliptic curve point to a byte string as described in SEC 1 v2.0 section 2.3.3.
    This method only supports uncompressed points.
    
    Args:
    point (cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePublicNumbers): 
        The elliptic curve point to encode.

    Returns:
    bytes: The encoded elliptic curve point.
    """
    # Load the elliptic curve
    curve = ec.SECP256R1()
    
    # Create an elliptic curve private key
    private_value = 12345
    private_key = ec.derive_private_key(
        private_value,
        curve,
        default_backend()
    )
    
    # Get the corresponding public key
    public_key = private_key.public_key()
    
    # Get the public numbers
    public_numbers = public_key.public_numbers()
    
    # Check if the given point is compatible with the public key
    if point.curve!= public_numbers.curve:
        raise ValueError("The given point is not compatible with the public key")
    
    # Encode the public key (point) in uncompressed format
    encoded_point = public_key.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.UncompressedPoint
    )
    
    return encoded_point

# Test the function
curve = ec.SECP256R1()
private_value = 12345
private_key = ec.derive_private_key(
    private_value,
    curve,
    default_backend()
)
public_key = private_key.public_key()
public_numbers = public_key.public_numbers()
encoded_point = encode_point(public_numbers)
print(encoded_point)
