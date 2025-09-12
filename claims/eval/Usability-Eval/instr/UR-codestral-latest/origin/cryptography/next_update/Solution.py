from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import datetime, timedelta

# Assuming CRL update is every 7 days
days_until_update = 7
next_update = datetime.now() + timedelta(days=days_until_update)

print(next_update)
