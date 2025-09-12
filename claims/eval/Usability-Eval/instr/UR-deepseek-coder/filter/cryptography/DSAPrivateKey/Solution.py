from cryptography.hazmat.primitives.asymmetric.dsa import DSAPrivateNumbers, DSAParameterNumbers
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os

# Generate DSA parameters
parameters = DSAParameterNumbers.generate_parameters(2048, default_backend())

# Generate DSA private key
private_key = DSAPrivateNumbers(
    x=int.from_bytes(os.urandom(32), 'big'),  # Private exponent
    public_numbers=parameters.generate_private_key().public_key().public_numbers()
).private_key(default_backend())

# Serialize the private key to PEM format
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

print(private_key_pem.decode())
