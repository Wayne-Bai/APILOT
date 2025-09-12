from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import datetime

# Load the CRL file
with open("path_to_crl_file.crl", "rb") as crl_file:
    crl_data = crl_file.read()

# Parse the CRL
crl = x509.load_der_x509_crl(crl_data, default_backend())

# Get the last updated time from the CRL
last_update = crl.last_update

# Convert the last update to a naive datetime object
naive_last_update = last_update.replace(tzinfo=None)

print("Last updated time (naive datetime):", naive_last_update)
