from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def deserialize_public_key(openssh_data):
    # Remove any whitespace and newlines from the data
    openssh_data = openssh_data.replace(" ", "").replace("\n", "")

    # Decode the base64 encoded data
    public_key_data = base64.b64decode(openssh_data)

    # Deserialize the public key
    public_key = rsa.RSAPublicKey.from_public_bytes(public_key_data)

    return public_key
