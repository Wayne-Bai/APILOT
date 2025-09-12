from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import datetime

# assuming crl_timestamp is the last update timestamp of the CRL
crl_timestamp = 1615446740  # for example
crl_last_update = datetime.fromtimestamp(crl_timestamp)

print(f"The CRL was last updated on: {crl_last_update}")
