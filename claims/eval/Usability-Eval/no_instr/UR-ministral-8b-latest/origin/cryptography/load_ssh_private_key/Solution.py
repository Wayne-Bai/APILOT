from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Supplied OpenSSH private key encoded in PEM format
ssh_private_key_pem = b"""
-----BEGIN OPENSSH PRIVATE KEY-----
MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyKkEyIPkiwEUiGRK+3/Z(+1 reactloop
TAv4N3B_D1vcY21e/wFSKXYfDboKuml6gptouPsdfIJjTqanLsmdQZC2yY4g==
-----END OPENSSH PRIVATE KEY-----
"""

# Deserialize OpenSSH private key
private_key_bytes = ssh_private_key_pem
private_key = serialization.load_pem_private_key(
    private_key_bytes,
    password=None,
    backend=default_backend()
)
print(private_key)
