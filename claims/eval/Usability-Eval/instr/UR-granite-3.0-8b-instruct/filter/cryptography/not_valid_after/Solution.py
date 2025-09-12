from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import datetime

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Get the notBefore and notAfter attributes from the private key
not_before = private_key.public_key().valid_from
not_after = private_key.public_key().valid_to

# Convert the notAfter attribute to a naive datetime in UTC
naive_datetime = not_after.replace(tzinfo=None)

print(naive_datetime)
