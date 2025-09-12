from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Generate a new DSA private key
private_key = serialization.dsa.generate_private_key(
    key_size=2048,  # This is the size of the key in bits
    backend=default_backend(),
)

# Get the public key from the private key
public_key = private_key.public_key()

# Serialize the public key to a string
public_key_string = public_key.encode(serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL)

print("DSA Public Key:")
print(public_key_string)
