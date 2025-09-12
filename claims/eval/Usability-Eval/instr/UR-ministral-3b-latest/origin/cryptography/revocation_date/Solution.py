from cryptography import x509
from datetime import datetime, timezone

# Initialize the date and time of the certificate revocation
cert_revocation_date = datetime.now(timezone.utc)

# Assume this is your naive datetime when the certificate is revoked
cert(value="10.10.2021 12:50:00.001")

# utilize cryptography.x509 Certificate construct though revocation details needs to be under scope using authored policy
