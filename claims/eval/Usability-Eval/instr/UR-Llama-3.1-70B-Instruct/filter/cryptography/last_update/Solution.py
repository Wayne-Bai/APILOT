from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend
from datetime import datetime

def get_last_update(crl_bytes):
    # Load the CRL from bytes
    crl = x509.load_der_x509_crl(crl_bytes, default_backend())

    # Get the last update date from the CRL
    last_update = crl.last_update

    # Convert the last update date to a naïve datetime object
    naive_last_update = last_update.replace(tzinfo=None)

    return naive_last_update

# Example usage:
crl_bytes = b'...'  # Your CRL bytes here
last_update = get_last_update(crl_bytes)
print(last_update)
