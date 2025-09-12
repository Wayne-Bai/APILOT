from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from datetime import datetime

# Assuming 'crl' is your Certificate Revocation List object
crl_last_update = crl.not_after

# Convert the datetime object to a string in ISO 8601 format
crl_last_update_str = crl_last_update.isoformat()

print(f"The last update of this CRL is: {crl_last_update_str}")
