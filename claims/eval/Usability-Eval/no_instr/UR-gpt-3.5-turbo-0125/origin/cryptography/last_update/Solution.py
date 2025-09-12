
from cryptography import x509
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat

# Load the CRL file
with open("crl.pem", "rb") as file:
    crl_data = file.read()

# Decode the CRL data
crl = x509.load_pem_x509_crl(crl_data)

# Get the last update time of the CRL
last_update_time = crl.last_update

print("Last update time of the CRL:", last_update_time)
