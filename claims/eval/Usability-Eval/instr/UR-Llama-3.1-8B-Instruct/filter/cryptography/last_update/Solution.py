from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import datetime
import base64

# Load the CRL from a file or a string
# For this example, let's assume we have a file named 'crl.der'
with open('crl.der', 'rb') as f:
    crl_data = f.read()

# Load the CRL
crl = x509.load_der_crl(crl_data, default_backend())

# Get the last update time
last_update = crl.last_update

# Convert the last update time to a naïve datetime object
naive_last_update = datetime.datetime(timestamp=last_update.timestamp(), tzinfo=None)

# Print the naïve datetime
print(naive_last_update)
