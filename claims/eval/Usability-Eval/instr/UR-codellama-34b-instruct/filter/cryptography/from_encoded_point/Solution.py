from cryptography import ec

def decode_sec_1_point(encoded_point):
    # Decode the byte string representing the elliptic curve point
    decoded_point = ec.EllipticCurvePoint._decode_byte_string(encoded_point)
    
    # Extract the x and y coordinates from the decoded point
    x, y = decoded_point[:32], decoded_point[32:]
    
    # Create an EllipticCurvePublicNumbers object from the coordinates
    return ec.EllipticCurvePublicNumbers(x, y)
