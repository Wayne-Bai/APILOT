from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.backends import default_backend

# Generate a DSA private key
dsa_gen_key = dsa.generate_private_key(
    public_exponent=2,
    key_size=2048,
    backend=default_backend()
)

print("Private key:", dsa_gen_key)
