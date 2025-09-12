from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding
from datetime import datetime, timedelta
import cryptography.hazmat.backends

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=cryptography.hazmat.backends.default_backend()
)

# Define the issuer and subject name of the certificate
issuer_name = x509.Name([
    x509.NameAttribute(x509.NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(x509.NameOID.STATE_OR_PROVINCE_NAME, u"California"),
    x509.NameAttribute(x509.NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(x509.NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(x509.NameOID.COMMON_NAME, u"mycompany.com"),
])

# Certificates are valid from the moment of creation.
valid_from = datetime.utcnow()

# The certificate will be valid for 1 year
valid_to = valid_from + timedelta(days=365)

# Create a certificate builder
certificate_builder = x509.CertificateBuilder(
    issuer_name=issuer_name,
    subject_name=issuer_name,
    public_key=private_key.public_key(),
    serial_number=x509.random_serial_number(),
    not_valid_before=valid_from,
    not_valid_after=valid_to
)

# Specify the hash algorithm
certificate_builder = certificate_builder.add_extension(
    x509.BasicConstraints(ca=True, path_length=3), critical=True)

# Self-sign the certificate
certificate = certificate_builder.sign(
    private_key=private_key,
    algorithm=hashes.SHA256(),
    backend=cryptography.hazmat.backends.default_backend()
)

# Export the certificate
cert_pem = certificate.public_bytes(encoding=Encoding.PEM)
print(cert_pem.decode())
