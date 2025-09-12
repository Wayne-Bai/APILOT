
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

# OpenSSH private key data
openssh_private_key_data = b'''
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABAY8kegkR
GG3ZKqK71AAAAEAAAAAEAAAAzLnRzZXJAY29tcHV0aWMub3JnAAAAAAAAAAEAAAAQAAAAEAA
AgFLoJi81fEY5PPzZ4dQjfP3bhoHQXW2C5k0Xebcal7i2t8BAAAAPXJlYWQtb3JnMvlSYsGF4
==DDDkdK/o5rRt9wBVjK9RvKOEc9+7RjtUdxO6R0IzVHh63RE42IESFqiq5bj7LZ
-----END OPENSSH PRIVATE KEY-----
'''

# Deserialize the private key
private_key = serialization.load_ssh_private_key(openssh_private_key_data, password=None, backend=default_backend())
