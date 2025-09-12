from cryptography.hazmat.primitives import serialization as ser
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_private_key():
    # Create new RSA private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Convert private key to bytes
    private_bytes = private_key.private_bytes(
        encoding=ser.Encoding.PEM,
        format=ser.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=ser.NoEncryption()
    )

    return private_bytes.decode()

private_key = generate_private_key()
print(private_key)
