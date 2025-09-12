from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from base64 import b64decode

def deserialize_privkey(ssh_encoded):
    """
    Deserialize a private key from OpenSSH encoded data to an instance of the private key type.
    
    Args:
    ssh_encoded (str): The OpenSSH encoded private key data
    
    Returns:
    PrivateKey: The deserialized private key instance
    """
    
    # Decode the base64 encoded private key
    decoded_data = b64decode(ssh_encoded.rstrip("\n"))
    
    # Construct the public and private numbers
    loaded = serialization.load_ssh_private_key(decoded_data, password=None, backend=default_backend())
    
    return loaded
