from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, BestAvailableEncryption
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta

# Generate a private key for creating a certificate
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Various details about who we are. For a self-signed certificate, the
# subject and issuer are always the same.
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Palo Alto"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mycompany.com"),
])

# Naive datetime for certificate validity start 
# (assumes now as the start time)
valid_from = datetime.utcnow()
# Naive datetime for certificate validity end (e.g., 1 year from now)
valid_to = valid_from + timedelta(days=365)

# Create the certificate
cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    valid_from
).not_valid_after(
    valid_to
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
    critical=False,
).sign(private_key, hashes.SHA256())

# Serialize and save the certificate to disk
cert_pem = cert.public_bytes(encoding=Encoding.PEM)
with open("selfsigned_certificate.pem", "wb") as f:
    f.write(cert_pem)

# Optional: Also serialize and save the private key
key_pem = private_key.private_bytes(
    encoding=Encoding.PEM,
    format=rsa.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=BestAvailableEncryption(b'mypassword')
)
with open("private_key.pem", "wb") as f:
    f.write(key_pem)

print("Certificate created with a naive end datetime of validity:", valid_to)
