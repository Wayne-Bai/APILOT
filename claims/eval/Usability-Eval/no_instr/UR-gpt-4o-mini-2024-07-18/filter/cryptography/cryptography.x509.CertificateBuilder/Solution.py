from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import datetime

def create_self_signed_cert(subject_name, issuer_name, public_key, serial_number):
    # Create a certificate builder
    builder = x509.CertificateBuilder()
    
    # Set the subject, issuer, and other fields
    builder = builder.subject_name(subject_name)
    builder = builder.issuer_name(issuer_name)
    builder = builder.public_key(public_key)
    builder = builder.serial_number(serial_number)
    builder = builder.not_valid_before(datetime.datetime.utcnow())
    builder = builder.not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))  # 1 year validity
    
    # Add extensions (if needed)
    builder = builder.add_extension(
        x509.BasicConstraints(ca=True, path_length=None),
        critical=True,
    )

    # Sign the certificate with the private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    
    certificate = builder.sign(
        private_key=private_key,
        algorithm=hashes.SHA256(),
        backend=default_backend()
    )
    
    return certificate, private_key

# Example Usage
subject = x509.Name([
    x509.NameAttribute(x509.NameOID.COMMON_NAME, u"My Test Certificate"),
])

issuer = x509.Name([
    x509.NameAttribute(x509.NameOID.COMMON_NAME, u"My Test Certificate"),
])

public_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
).public_key()

cert, private_key = create_self_signed_cert(subject, issuer, public_key, serial_number=123456)

# Save the certificate and private key to files
with open("certificate.pem", "wb") as cert_file:
    cert_file.write(cert.public_bytes(serialization.Encoding.PEM))

with open("private_key.pem", "wb") as key_file:
    key_file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))
