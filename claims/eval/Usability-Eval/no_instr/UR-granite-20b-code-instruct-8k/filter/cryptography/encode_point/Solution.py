from cryptography.hazmat.primitives.asymmetric import ec

def encode_point(point):
    if point.curve.name != "SECP256R1":
        raise ValueError("Unsupported curve")
    if point.order != 0 and point.order != ec.SECP256R1.generator.order():
        raise ValueError("Invalid point")
    if point. infinity:
        raise ValueError("Point cannot be infinity")
    x_bytes = point.x.to_bytes(32, byteorder="big", signed=False)
    y_bytes = point.y.to_bytes(32, byteorder="big", signed=False)
    return b"\x04" + x_bytes + y_bytes
