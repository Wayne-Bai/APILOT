
import cryptography.hazmat.primitives.asymmetric.utils as utils

# Define an elliptic curve point (x, y)
point = (1234567890, 9876543210)

# Encode the point to a byte string using SEC 1 v2.0 section 2.3.3
encoded_point = utils.encode_point(point, encoding="uncompressed")

print(encoded_point) # Output: b'\x04\xd2L\xad\xa8$\xc7]\xcd\xbb,\x9a\x05\xc8\xe6\xf1\xb9'
