from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import datetime

# Function to load a CRL from a PEM file
def load_crl_from_pem(pem_file_path):
    with open(pem_file_path, 'rb') as pem_file:
        crl_data = pem_file.read()
    crl = x509.load_pem_x509_crl(crl_data, default_backend())
    return crl

# Function to retrieve the last update time of a CRL
def get_crl_last_update(crl):
    last_update = crl.last_update
    # Converting to a naive datetime object (no timezone awareness)
    last_update_naive = last_update.replace(tzinfo=None)
    return last_update_naive

# Example usage
# Load the CRL
crl = load_crl_from_pem("path_to_crl.pem")

# Get the last update as a naive datetime
naive_last_update = get_crl_last_update(crl)
print("CRL was last updated on:", naive_last_update)
