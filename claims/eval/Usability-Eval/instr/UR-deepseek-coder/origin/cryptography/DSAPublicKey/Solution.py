from cryptography.hazmat.primitives.asymmetric.dsa import DSAPublicKey, DSAParameters, DSAPublicNumbers
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Generate DSA parameters
parameters = DSAParameters.generate(2048, default_backend())

# Generate a DSA private key
private_key = parameters.generate_private_key()

# Derive the public key from the private key
public_key = private_key.public_key()

# Serialize the public key to PEM format
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print(public_key_pem.decode())
