from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend

# Generate a DSA private key
def generate_dsa_private_key(key_size=2048):
    private_key = dsa.generate_private_key(
        key_size=key_size,
        backend=default_backend()
    )
    return private_key

# Example usage
dsa_private_key = generate_dsa_private_key()
print("DSA Private Key:", dsa_private_key)
