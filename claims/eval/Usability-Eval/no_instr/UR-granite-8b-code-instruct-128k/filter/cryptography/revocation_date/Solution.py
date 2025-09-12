from cryptography import x509
from datetime import datetime

# Load the certificate from a file or other source
with open("certificate.pem", "rb") as certificate_file:
    certificate = x509.load_pem_x509_certificate(certificate_file.read())

# Check if the certificate has been revoked
if certificate. Revoked:
    # If the certificate has been revoked, get the revocation date
    revocation_date = certificate.Revoked.RevocationDate
    # Convert the revocation date from naive to aware (UTC)
    revocation_date_aware = revocation_date.replace(tzinfo=datetime.utcnow().tzinfo)
    print(revocation_date_aware)
else:
    print("This certificate has not been revoked.")
