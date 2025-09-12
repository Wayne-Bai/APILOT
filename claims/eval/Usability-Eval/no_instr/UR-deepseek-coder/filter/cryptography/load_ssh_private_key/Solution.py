from cryptography.hazmat.primitives.serialization import load_ssh_private_key
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec
from cryptography.hazmat.backends import default_backend
import base64

def deserialize_private_key(openssh_data):
    # Decode the base64 encoded OpenSSH private key data
    decoded_data = base64.b64decode(openssh_data)
    
    # Load the private key using cryptography
    private_key = load_ssh_private_key(decoded_data, password=None, backend=default_backend())
    
    # Determine the type of the private key
    if isinstance(private_key, rsa.RSAPrivateKey):
        key_type = "RSA"
    elif isinstance(private_key, dsa.DSAPrivateKey):
        key_type = "DSA"
    elif isinstance(private_key, ec.EllipticCurvePrivateKey):
        key_type = "EC"
    else:
        key_type = "Unknown"
    
    return private_key, key_type

# Example usage
openssh_data = "base64_encoded_openssh_private_key_data"
private_key, key_type = deserialize_private_key(openssh_data)
print(f"Deserialized {key_type} private key")
