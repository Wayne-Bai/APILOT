from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Subject and issuer details
subject = x509.Name([
    x509.NameAttribute(x509.NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(x509.NameOID.STATE_OR_PROVINCE_NAME, u"California"),
    x509.NameAttribute(x509.NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(x509.NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(x509.NameOID.COMMON_NAME, u"mycompany.com"),
])

# Create a self-signed certificate
certificate = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(subject)  # Self-signed, so subject and issuer are the same
    .public_key(private_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))  # Valid for 1 year
    .add_extension(
        x509.BasicConstraints(ca=True, path_length=None), critical=True
    )
    .sign(private_key, hashes.SHA256(), default_backend())
)

# Save the private key and certificate to files
with open("private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=x509.Encoding.PEM,
        format=x509.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=x509.NoEncryption()
    ))

with open("certificate.pem", "wb") as f:
    f.write(certificate.public_bytes(encoding=x509.Encoding.PEM))
