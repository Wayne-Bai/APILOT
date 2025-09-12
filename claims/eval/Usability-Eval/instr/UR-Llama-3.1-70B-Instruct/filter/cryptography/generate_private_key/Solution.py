from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def generate_rsa_private_key(key_size: int = 2048) -> rsa.RSAPrivateKey:
    """
    Generates a new RSA private key.

    Args:
    - key_size (int): The size of the key in bits. Defaults to 2048.

    Returns:
    - rsa.RSAPrivateKey: A new RSA private key.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )
    return private_key

def write_private_key_to_pem_file(private_key: rsa.RSAPrivateKey, filename: str) -> None:
    """
    Writes the private key to a PEM file.

    Args:
    - private_key (rsa.RSAPrivateKey): The RSA private key to write.
    - filename (str): The filename to write the private key to.
    """
    with open(filename, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

# Example usage:
private_key = generate_rsa_private_key()
write_private_key_to_pem_file(private_key, "private_key.pem")
