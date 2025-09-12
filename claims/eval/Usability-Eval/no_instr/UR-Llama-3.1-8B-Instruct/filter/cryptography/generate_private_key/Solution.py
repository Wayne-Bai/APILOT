from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_rsa_private_key():
    """
    Generates a new RSA private key.
    """
    # Generate a new RSA key with a key size of 2048 bits
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Serialize the private key to a PEM encoded string
    private_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Serialize the public key to a PEM encoded string
    public_pem = key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Return the private and public key as strings
    return private_pem.decode('utf-8'), public_pem.decode('utf-8')

# Generate the RSA private and public key
private_key, public_key = generate_rsa_private_key()

# Print the private and public key
print("Private Key ( RSA 2048 bits ) :")
print(private_key)
print("\nPublic Key ( RSA 2048 bits ) :")
print(public_key)
