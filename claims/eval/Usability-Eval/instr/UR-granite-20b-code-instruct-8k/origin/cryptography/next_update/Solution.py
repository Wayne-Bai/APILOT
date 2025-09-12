from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Load the certificate
with open("certificate.pem", "rb") as f:
    cert = x509.load_pem_x509_certificate(f.read(), default_backend())

# Extract the notAfter field from the certificate's validity period
next_update = cert.not_valid_after

# Print the result
print("The next update to this CRL is expected on:", next_update)
