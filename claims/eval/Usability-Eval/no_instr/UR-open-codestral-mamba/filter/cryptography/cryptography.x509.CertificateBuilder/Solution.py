# Import necessary libraries
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# Generate a private key
def generate_private_key():
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

# Generate a self-signed certificate
def generate_self_signed_cert(private_key, issuer, subject):
    # Basic constraints for a self-signed certificate
    basic_constraints = x509.BasicConstraints(ca=True, path_length=None)

    # Create the certificate
    cert = x509.CertificateBuilder()\
        .subject_name(subject)\
        .issuer_name(issuer)\
        .public_key(private_key.public_key())\
        .serial_number(x509.random_serial_number())\
        .not_valid_before(datetime.datetime.utcnow())\
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))\
        .add_extension(basic_constraints, critical=True)\
        .sign(private_key, hashes.SHA256(), default_backend())

    return cert

# Generate the private key
private_key = generate_private_key()

# Set the issuer and subject
issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, u"localhost")])
subject = issuer

# Generate the self-signed certificate
cert = generate_self_signed_cert(private_key, issuer, subject)

# To save the created certificate
with open("localhost.crt", "wb") as f:
    f.write(cert.public_bytes(encoding=serialization.Encoding.PEM))
