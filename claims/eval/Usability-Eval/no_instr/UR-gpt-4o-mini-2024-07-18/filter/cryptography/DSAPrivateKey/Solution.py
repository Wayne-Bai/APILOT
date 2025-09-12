from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

# Generate a DSA private key
private_key = dsa.generate_private_key(
    key_size=2048,  # You can adjust the key size
    backend=default_backend()
)

# Serialize the private key to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()  # Change to DefaultEncryption if you need encryption
)

# Write the private key to a file
with open('dsa_private_key.pem', 'wb') as f:
    f.write(private_pem)

print("DSA private key generated and saved to 'dsa_private_key.pem'.")
