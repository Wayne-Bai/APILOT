from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Generate a new RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,  # You can choose 2048 or larger for more security
    backend=default_backend()
)

# You might want to serialize the private key to store it
pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()  # Use encryption here for additional security when saving the key
)

# Print the PEM encoded private key
print(pem_private_key.decode('utf-8'))
