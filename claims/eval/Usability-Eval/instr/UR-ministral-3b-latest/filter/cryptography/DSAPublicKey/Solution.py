import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
import rsa

# Generate RSA private key and public key
private_key, public_key = rsa.newkeys(2048)

# Serialize and save the keys to PEM format
with open("private.pem", "wb") as private_file, open("public.pem", "wb") as public_file:
    private_file.write(private_key.exportPEM())
    public_file.write(public_key.exportPEM())
