from cryptography import x509
from cryptography.x509.oid import ExtensionOID
from cryptography.x509 import InvalidVersion

# Create a naive datetime representing the date this certificate was revoked
revocation_date = "2023-09-15T12:00:00"
