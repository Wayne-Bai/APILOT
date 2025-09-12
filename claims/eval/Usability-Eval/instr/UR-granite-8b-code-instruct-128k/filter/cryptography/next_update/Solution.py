from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Load the CRL from a file
with open("crl.pem", "rb") as crl_file:
    crl_data = crl_file.read()

crl = x509.load_pem_crl(crl_data, default_backend())

# Get the next update time from the CRL
next_update = crl.next_update

# Print the next update time
print("Next update time:", next_update)
