from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

def create_self_signed_cert():
    # Generate our key
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Create our self-signed certificate
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, u"localhost"),
    ])

    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        # Must be at least a day from the current time
    ).not_valid_after(
        # Must be at least one year from the current time
    ).add_extension(
        x509.BasicConstraints(ca=True, path_length=None), critical=True,
    ).sign(key, hashes.SHA256(), default_backend())

    # Write our certificate out to disk.
    with open("selfsigned.pem", "wb") as f:
        f.write(cert.public_bytes(x509.Encoding.PEM))

    # Write our key out to disk.
    with open("privateKey.pem", "wb") as f:
        f.write(key.private_bytes(
            encoding=x509.Encoding.PEM,
            format=x509.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=x509.NoEncryption(),
        ))

create_self_signed_cert()
