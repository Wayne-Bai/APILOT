
import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

def decode_public_key(encoded_key):
    # Decode the encoded key
    decoded_key = bytes.fromhex(encoded_key)

    # Determine if the key is compressed or uncompressed
    compressed_header = b'\x02'
    uncompressed_header = b'\x04'
    header = decoded_key[:1]
    if header == compressed_header:
        # Decode the point from the compressed format
        y_parity = (decoded_key[1] & 2) // 2
        x = ec.derive_public_key(b'\x04' + decoded_key[1:] + b'\x00', 3, 'ecdsa-with-SHA256').public_numbers().x()
        y = ec.derive_public_key(b'\x04' + decoded_key[1:] + (y_parity).to_bytes(1, "big"), 3, 'ecdsa-with-SHA256').public_numbers().y()
    else:
        # Decode the point from the uncompressed format
        x = ec.derive_public_key(b'\x04' + decoded_key[1:], 3, 'ecdsa-with-SHA256').public_numbers().x()
        y = ec.derive_public_key(b'\x04' + decoded_key[1:], 3, 'ecdsa-with-SHA256').public_numbers().y()
    
    # Return the decoded point as an EllipticCurvePublicNumbers object
    return ec.EllipticCurvePublicNumbers(x, y, ec.SECP256K1())
