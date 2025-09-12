from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives.asymmetric.dsa import DSAPrivateKey
from cryptography.hazmat.backends import default_backend

# Generate a DSA private key
def generate_dsa_private_key():
    private_key = dsa.generate_private_key(key_size=1024, backend=default_backend())
    return private_key

# Generate a DSA private key
private_key = generate_dsa_private_key()

# Display the private key information
print(private_key)
