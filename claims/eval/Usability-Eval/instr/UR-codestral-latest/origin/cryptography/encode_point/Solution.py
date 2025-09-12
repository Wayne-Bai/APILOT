from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

def encode_ec_point(point):
    x_coord = point.x.to_bytes((point.curve.key_size + 7) // 8, 'big')
    y_coord = point.y.to_bytes((point.curve.key_size + 7) // 8, 'big')

    encoded_point = b'\x04' + x_coord + y_coord
    return encoded_point
