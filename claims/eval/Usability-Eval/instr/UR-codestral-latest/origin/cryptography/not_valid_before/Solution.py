from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from datetime import datetime, timedelta
import pytz

# Creating a naive datetime object representing the beginning of the validity period for the certificate in UTC
not_before = datetime.now(pytz.UTC)

# Print the created datetime object
print(f'Not Before: {not_before}')
