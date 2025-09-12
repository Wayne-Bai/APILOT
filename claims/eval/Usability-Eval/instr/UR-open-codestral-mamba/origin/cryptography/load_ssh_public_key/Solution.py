from cryptography.hazmat.primitives.asymmetric import serialization
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.backends import default_backend as crypto_default_backend

def deserialize_public_key(data):
    backend = crypto_default_backend()
    key_bytes = compute_key_bytes(data)
    public_key = crypto_serialization.load_ssh_public_key(key_bytes, backend)
    return public_key

def compute_key_bytes(data):
    if data.startswith("ssh-rsa "):
        # Decode the base64 RSA public key
        return base64.b64decode(data.split(" ")[1])
    elif data.startswith("ecdsa-sha2-nistp256 "):
        # Decode the base64 ECDSA key
        enc_bytes = base64.b64decode(data.split(" ")[1].encode("utf-8"))
        # Extract the x and y coordinates and concatenate them to form the key bytes
        intlen = 32 if len(enc_bytes) == 65 else 20
        return enc_bytes[1:intlen+1] + enc_bytes[1+intlen:2*intlen+1]
    else:
        raise ValueError("Unsupported SSH key type.")
