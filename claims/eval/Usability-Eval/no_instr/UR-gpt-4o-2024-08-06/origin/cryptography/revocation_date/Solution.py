from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from datetime import datetime

# Example: Load a certificate revocation list (CRL) from a file
with open("example_crl.pem", "rb") as crl_file:
    crl_data = crl_file.read()

# Parse the CRL
crl = x509.load_pem_x509_crl(crl_data, default_backend())

# Iterate over each revoked certificate in the CRL
for revoked_cert in crl:
    # Get the serial number of the revoked certificate
    serial_number = revoked_cert.serial_number
    # Get the date this certificate was revoked
    revocation_date = revoked_cert.revocation_date

    # Print the revocation details
    print(f"Certificate with serial number {serial_number} was revoked on {revocation_date}.")
