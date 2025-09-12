# Importing required libraries
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend

def generate_dsa_keypair():
    # Generate DSA key pair
    key = dsa.generate_private_key(
        key_size=2048,
        backend=default_backend()
    )
    
    # Get private key in PEM format
    private_key = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    # Get public key in PEM format
    public_key = key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    return private_key, public_key

def main():
    private_key, public_key = generate_dsa_keypair()
    
    # Print keys
    print("Private Key:")
    print(private_key.decode('utf-8'))
    print("Public Key:")
    print(public_key.decode('utf-8'))

if __name__ == "__main__":
    main()
