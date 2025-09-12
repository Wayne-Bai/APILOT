# Import necessary libraries
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend

# Generate a new DSA private key
private_key = dsa.generate_private_key(
    key_size=2048,
    backend=default_backend()
)

# Serialize the private key for storage or transmission
pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Example usage: Print the private key in PEM format
print(pem_private_key.decode("utf-8"))

# To verify, let's create a DSA signature and then verify it.
# Generate a signature
signature = private_key.sign(b"This is the message to sign", dsa.sha256())

# Extract the corresponding public key
public_key = private_key.public_key()

# Verify the signature
try:
    public_key.verify(signature, b"This is the message to sign", dsa.sha256())
    print("The signature is valid.")
except:
    print("The signature is not valid.")

# If needed, serialize the public key for storage or transmission
pem_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print("Public Key in PEM format:")
print(pem_public_key.decode("utf-8"))
