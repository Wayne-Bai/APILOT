from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

# Generate a private key
def generate_private_key():
    # Generate a 2048-bit DSA private key
    private_key = dsa.generate_private_key(
        key_size=2048,
        public_exponent=2,
    )

    # Private bytes
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    return pem.decode('utf-8')

# Print the generated private key
private_key = generate_private_key()
print(private_key)
