
import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

# Import OpenSSH RFC 4253 and PROTOCOL.certkeys encoded data
encoded_data = ...

# Deserialize the public key from the encoded data
with open(encoded_data, 'rb') as f:
    serialized_key = base64.b64decode(f.read())
public_key = serialization.load_ssh_public_key(serialized_key)

# Print the public key in OpenSSH format
print(public_key.get_name())
