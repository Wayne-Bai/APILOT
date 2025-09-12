import datetime
import cryptography
from cryptography.x509 import CertificateBuilder
from cryptography.x509.oid import NameOID
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_certificate(hostname, private_key):
    issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"CA"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"My Company Root CA"),
    ])

    subject = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, hostname),
    ])

    builder = x509.CertificateBuilder()
    builder = builder.subject_name(subject)
    builder = builder.issuer_name(issuer)
    builder = builder.not_valid_before(datetime.datetime.today())
    builder = builder.not_valid_after(datetime.datetime.today() + datetime.timedelta(days=365))
    builder = builder.serial_number(x509.random_serial_number())
    builder = builder.public_key(private_key.public_key())
    builder = builder.add_extension(x509.SubjectAlternativeName([x509.DNSName(hostname)]), critical=False,)
    builder = builder.add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True,)

    cert = builder.sign(private_key=private_key, algorithm=hashes.SHA256(), backend=default_backend())

    return cert

# Generate private key
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

with open("private_key.pem", "wb") as key_file:
    key_file.write(private_key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.TraditionalOpenSSL, serialization.NoEncryption()))

hostname = "your_domain.com"
cert = generate_certificate(hostname, private_key)
cert_pem = cert.public_bytes(serialization.Encoding.PEM)

with open("cert_file.pem", "wb") as cert_file:
    cert_file.write(cert_pem)
