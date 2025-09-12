# Importing necessary libraries
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from datetime import datetime, timedelta
import pytz

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Create a subject and issuer
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mycompany.com"),
])

# Define the certificate's validity period
validity_start = datetime(2024, 1, 1)
validity_start = validity_start.replace(tzinfo=pytz.UTC)  # Make it timezone aware
validity_end = validity_start + timedelta(days=365)

# Create the certificate
cert = (
    x509.CertificateBuilder()
   .subject_name(subject)
   .issuer_name(issuer)
   .public_key(private_key.public_key())
   .serial_number(x509.random_serial_number())
   .not_valid_before(validity_start) # replaced by naive datetime object which correctly indicates the value is interpreted in UTC.
   .not_valid_after(validity_end)
   .add_extension(x509.SubjectAlternativeName([x509.DNSName(u"localhost")]), critical=False)
   .sign(private_key, hashes.SHA256(), default_backend())
)

# Save the certificate to a file
with open("certificate.crt", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))
