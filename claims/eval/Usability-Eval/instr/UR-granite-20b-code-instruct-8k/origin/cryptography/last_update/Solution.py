from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Load the CRL from disk
with open("crl.pem", "rb") as f:
    crl_data = f.read()
crl = x509.load_crl(crl_data)

# Get the last update time
last_update = crl.last_update_time

# Print the last update time
print(last_update)
