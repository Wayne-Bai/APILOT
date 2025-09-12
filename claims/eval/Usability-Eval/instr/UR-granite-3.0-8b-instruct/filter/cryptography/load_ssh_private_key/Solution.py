from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def deserialize_private_key(data: bytes) -> serialization.LoadingKey:
    return serialization.load_pem_private_key(
        data,
        password=None,  # If the key is encrypted, provide the password here
        backend=default_backend()
    )
