from cryptography import x509
from datetime import datetime, timedelta

# Create a naive datetime object representing the beginning of the validity period in UTC
validity_start = datetime.utcnow()

# Example: Create a naive datetime representing the end of the validity period (1 year later)
validity_end = validity_start + timedelta(days=365)

print("Validity Start:", validity_start)
print("Validity End:", validity_end)
