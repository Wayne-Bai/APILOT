from cryptography import hmac
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

import hashlib
from base64 import b64encode, b64decode
import datetime

# Generate a new private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()

# Generate a symmetric key
symmetric_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=256,
    private_numbers=private_key.private_numbers()
).private_numbers().private_key

# Sample message
message = b"Sample Message to be encrypted"

# Digital signature
signature = public_key.sign(
    message,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Encode the message and signature
msg_with_sig = b''.join([message, signature])

# Create a HMAC
hmac_key = b"SecretKey"
hmac_hash = hmac.HMAC(
    symmetric_key,
    msg_with_sig,
    () if msg_with_sig == b'' else hmac._HMAC()._hmac_salt(None)
)

encrypted_msg = hmac_hash.digest()

# Decrypt message using symmetric key
decrypted_msg = symmetric_key.decrypt(encrypted_msg)

# Check if the decrypted message matches the original message
assert decrypted_msg == message

# Date of CRL last update
crl_last_update = datetime.datetime.now()

print(f"CRL last updated on {crl_last_update}")
