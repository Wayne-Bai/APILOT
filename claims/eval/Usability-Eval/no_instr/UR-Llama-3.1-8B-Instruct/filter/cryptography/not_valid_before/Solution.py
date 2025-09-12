from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization
from datetime import datetime, timedelta

# Define the validity period start and end dates
validity_start_date = datetime.utcnow()
validity_end_date = validity_start_date + timedelta(days=365)

# Example usage can go here
print(f"Validity start date: {validity_start_date}")
print(f"Validity end date: {validity_end_date}")
