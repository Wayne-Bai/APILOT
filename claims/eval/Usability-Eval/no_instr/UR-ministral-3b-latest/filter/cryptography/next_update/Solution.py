from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.gostrf import GOST2000PCL4c12
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime

# Generate a private key
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Create a public key object
public_key = private_key.public_key()

# Convert private key to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)

# Convert public key to PEM format
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

# Set a custom expiration datetime to represent when the CRL will expire
crl_update_expected = datetime(2022, 12, 31)

# Display the private key, public key, and the expected CRL update datetime
print("Private Key:", private_pem)
print("Public Key:", public_pem)
print("CRL Update Expected:", crl_update_expected)
