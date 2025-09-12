# Importing necessary libraries from cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend

def generate_dsa_public_key():
    """
    Generate a DSA public key.
    
    Returns:
    bytes: DSA public key in PEM format
    """
    
    # Generate a new DSA key pair
    key = dsa.generate_private_key(key_size=2048,
                                   backend=default_backend())
    
    # Get the DSA public key
    public_key = key.public_key()
    
    # Serialize the DSA public key to PEM format
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo)
    
    return pem

def main():
    # Generate a DSA public key
    public_key_pem = generate_dsa_public_key()
    
    # Print the DSA public key
    print(public_key_pem.decode('utf-8'))

if __name__ == "__main__":
    main()
