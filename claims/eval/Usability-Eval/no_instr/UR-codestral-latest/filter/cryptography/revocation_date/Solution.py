from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import NameOID
import datetime

# Generate private key
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

# Create subject
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"www.example.com"),
])

# Create certificate
cert = x509.CertificateBuilder().subject_name(subject)\
    .issuer_name(issuer)\
    .public_key(private_key.public_key())\
    .serial_number(x509.random_serial_number())\
    .not_valid_before(datetime.datetime.utcnow())\
    .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))\
    .add_extension(x509.RevokedCertificateBuilder().revocation_date(datetime.datetime(2022, 1, 1)), critical=False)\
    .sign(private_key, hashes.SHA256(), default_backend())

# Write certificate to file
with open("certificate.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))
