from cryptography import x509
from datetime import datetime

# Create a new CRL (Certificate Revocation List)
crl = x509.CertificateRevocationList()

# Set the expected update time
expected_update_time = datetime(2022, 12, 31)

# Set the next update time (e.g., 1 day later)
next_update_time = expected_update_time + timedelta(days=1)

# Add the next update time to the CRL
crl.next_update_time = next_update_time

# Print the CRL with the expected update time and next update time
print(crl)
