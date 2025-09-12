
from datetime import datetime, timedelta
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# Calculate the next update time for the CRL
next_update = crl.next_update  # Assuming crl is the CertificateRevocationList object
if next_update:
    naive_next_update = next_update.replace(tzinfo=None)
    print("Naïve datetime for next update:", naive_next_update)
