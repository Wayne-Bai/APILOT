
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Convert OpenSSH public key to PEM format
def openssh_to_pem(openssh_key):
    # Strip "ssh-rsa" or "ecdsa-sha2-nistp256" from the start of the key, if present
    if openssh_key.startswith("ssh-rsa") or openssh_key.startswith("ecdsa-sha2-nistp256"):
        openssh_key = openssh_key[4:]
    # Convert to base64 encoded string
    key_b64 = base64.b64encode(openssh_key)
    # Create a PEM certificate with the public key
    pem_cert = "-----BEGIN CERTIFICATE-----\n" + key_b64 + "\n-----END CERTIFICATE-----\n"
    return pem_cert

# Load the OpenSSH public key from a file
with open("public_key.txt", "r") as f:
    openssh_key = f.read()

# Convert to PEM format
pem_cert = openssh_to_pem(openssh_key)

# Print the PEM certificate
print(pem_cert)
