from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import datetime

# Assuming you have the CRL data in 'crl_bytes'
# For demonstration, let's create a sample CRL with an updated datetime.
# In practice, you would load your actual CRL bytes.

# Create a sample CRL (In real scenarios, this would be loaded from an actual CRL)
crl_builder = x509.CertificateRevocationListBuilder()

# Assume the CRL was last updated at the current datetime
last_updated = datetime.utcnow()

# Set the last update datetime
crl_builder = crl_builder.lastUpdate(last_updated)

# Print the last updated time
print("The Certificate Revocation List was last updated on:", last_updated)
