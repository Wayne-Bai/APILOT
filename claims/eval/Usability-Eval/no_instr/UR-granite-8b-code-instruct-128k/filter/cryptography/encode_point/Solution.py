from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

def encode_point(point):
    encoded_point = point.encode(serialization.Encoding.SEC1, serialization.PublicFormat.Uncompressed)
    return encoded_point
