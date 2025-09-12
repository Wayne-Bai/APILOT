from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import datetime

# Load the private key
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

# Load the certificate
with open("certificate.pem", "rb") as cert_file:
    certificate = x509.load_pem_x509_certificate(
        cert_file.read(),
        backend=default_backend()
    )

# Get the notBefore and notAfter dates from the certificate
not_before = certificate.notBefore
not_after = certificate.notAfter

# Create a datetime object for the current date and time
now = datetime.datetime.utcnow()

# Calculate the difference between the notAfter date and the current date and time
diff = not_after - now

# Print the result
print(f"The certificate will be revoked on {diff.days} days.")
