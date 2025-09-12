from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

def encode_point_to_bytes(point):
    encoded_point = point.encode(
        encoding=serialization.Encoding.SEC1,
        compression=serialization.Compression.UNCOMPRESSED
    )
    return encoded_point
