# Importing required libraries from cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_dsa_public_key():
    # Generating a public/private key pair using RSA algorithm
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    
    # Getting the private bytes
    private_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    # Getting the public bytes
    public_pem = key.public_key().public_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PublicFormat.OpenSSH
    )
    
    return private_pem, public_pem

# Generating the public key
private_key, public_key = generate_dsa_public_key()
print("Private Key:")
print(private_key.decode('utf-8'))
print("\nPublic Key:")
print(public_key.decode('utf-8'))
