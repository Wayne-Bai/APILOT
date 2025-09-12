from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa

def generate_dsa_public_key():
    # Generate a private key
    private_key = dsa.generate_private_key(key_size=1024)

    # Generate the public key based on the private key
    public_key = private_key.public_key()

    # Serialize public key to bytes
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return pem

public_key = generate_dsa_public_key()
print(public_key)
