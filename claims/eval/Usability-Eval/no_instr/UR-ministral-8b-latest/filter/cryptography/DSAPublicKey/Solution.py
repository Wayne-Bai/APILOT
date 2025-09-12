from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa

# Generate a DSA private key
private_key = dsa.generate_private_key(
    parameter_spec=dsa.generate_parameters(
        generation_backend=default_backend(),
        exponent=2048,
        hash_algorithm="SHA512"
    )
)

# Derive the public key from the private key
public_key = private_key.public_key()

# Use the public key
print("DSA Public Key (in PEM format):")
print(public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
))
