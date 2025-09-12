from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# sample ssh key data
ssh_key_data = b"your-ssh-key-data-here"

# use the default backend
backend = default_backend()

# deserialize the private key
private_key = serialization.load_ssh_private_key(ssh_key_data, password=None, backend=backend)

# check the key type
if isinstance(private_key, rsa.RSAPrivateKey):
    print("The private key is of RSA type.")
else:
    print("The private key is of a different type.")
