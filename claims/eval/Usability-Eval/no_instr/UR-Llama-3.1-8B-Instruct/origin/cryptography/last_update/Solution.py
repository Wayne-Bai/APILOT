from cryptography import x509
from cryptography.x509.oid import NameOID
from datetime import datetime

# Load the CRL from a file (replace with your file path)
with open('crl.der', 'rb') as f:
    crl_der = f.read()

# Load the CRL
crl = x509/load_der_x509_crl(crl_der)

# Get the last update time
last_update = crl.last_update

# Convert the last update time to a datetime object
last_update_datetime = datetime.fromtimestamp(last_update.timestamp())

print("The CRL was last updated on: ", last_update_datetime)
