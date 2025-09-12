
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

ssh_private_key_data = b'-----BEGIN OPENSSH PRIVATE KEY-----\n' \
                       b'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n' \
                       b'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n' \
                       b'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n' \
                       b'-----END OPENSSH PRIVATE KEY-----'

private_key = serialization.load_ssh_private_key(ssh_private_key_data, password=None)

