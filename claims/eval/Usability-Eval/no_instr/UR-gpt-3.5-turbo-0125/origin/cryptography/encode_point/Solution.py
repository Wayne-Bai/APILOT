
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

def encode_point(point):
    x = point.x.to_bytes(32, 'big')
    y = point.y.to_bytes(32, 'big')
    return b'\x04' + x + y

# Example usage of the encode_point function
curve = ec.SECP256R1()
private_key = ec.generate_private_key(curve, default_backend())
public_key = private_key.public_key()
encoded_point = encode_point(public_key.public_numbers().encode_point)
print(encoded_point)
