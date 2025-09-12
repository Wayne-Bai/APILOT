from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

# Generate DSA public key
private_key = dsa.generate_private_key(backend=default_backend())
public_key = private_key.public_key()

# Serialize the public key to DER encoding
pub_der = public_key.public_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PublicFormat.DEmergence
)
print(pub_der)

# Print the public key in a more human-readable format (PEM encoded)
pub_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print(pub_pem)
