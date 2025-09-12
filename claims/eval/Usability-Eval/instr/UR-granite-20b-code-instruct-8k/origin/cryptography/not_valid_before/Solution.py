from cryptography import x509
from cryptography.hazmat.primitives import datetime

# Generate a naive datetime representing the beginning of the validity period for the certificate in UTC
not_before = datetime.datetime(2023, 1, 1, 0, 0, 0)
