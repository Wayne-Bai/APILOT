from cryptography import x509
from cryptography.x509.oid import ExtensionOID
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import datetime

# Load your certificate and CRL (Certificate Revocation List) - replace 'your_certificate.pem' and 'your_crl.pem' with your actual file paths
with open("your_certificate.pem", "rb") as cert_file:
    cert_data = cert_file.read()
    certificate = x509.load_pem_x509_certificate(cert_data, default_backend())

with open("your_crl.pem", "rb") as crl_file:
    crl_data = crl_file.read()
    crl = x509.load_pem_x509_crl(crl_data, default_backend())

# Check if the certificate is revoked and print the revocation date
revoked_cert = None
for r in crl:
    if r.serial_number == certificate.serial_number:
        revoked_cert = r
        break

if revoked_cert:
    print(f"Certificate was revoked on: {revoked_cert.revocation_date}")
else:
    print("Certificate is not on the revocation list.")
