from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import datetime

# Example: Load a CRL (Certificate Revocation List) from a file
with open('your_crl.pem', 'rb') as crl_file:
    crl_data = crl_file.read()

# Load the CRL
crl = x509.load_pem_x509_crl(crl_data, default_backend())

# Get the lastUpdate time
last_updated = crl.last_update

# Print the last updated time
print("CRL Last Updated:", last_updated)
