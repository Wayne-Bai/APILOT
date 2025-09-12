from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import openssh, rsa
from cryptography.hazmat.backends import default_backend

def deserialize_public_key(encoded_data):
    # Decode the base64 encoded data
    decoded_data = base64.b64decode(encoded_data)

    # Deserialize the OpenSSH public key
    openssh_key = openssh.OpenSSHPublicKey.from_public_bytes(decoded_data, backend=default_backend())

    # If the key is an RSA key, convert it to an RSA key
    if isinstance(openssh_key, rsa.RSAPublicKey):
        rsa_key = rsa.RSAPublicKey.from_public_bytes(openssh_key.public_bytes(), backend=default_backend())
    else:
        rsa_key = openssh_key

    return rsa_key

# Example usage
encoded_data = b'...'  # Replace with the encoded data
public_key = deserialize_public_key(encoded_data)
