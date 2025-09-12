
import cryptography
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import NameOID

# Generate a private key using cryptography
private_key = serialization.load_pem_private_key(open("private.pem", "rb").read(), None)

# Generate a X.509 certificate builder
builder = x509.CertificateBuilder()

# Set the subject of the certificate to be the issuing CA
subject = builder.subject_name()
subject.common_name = "My Company"
subject.country_name = "US"
subject.state_or_province_name = "California"
subject.locality_name = "San Francisco"

# Set the issuer of the certificate to be the issuing CA
issuer = builder.issuer_name()
issuer.common_name = "My Company"
issuer.country_name = "US"
issuer.state_or_province_name = "California"
issuer.locality_name = "San Francisco"

# Set the validity period of the certificate
not_before = builder.not_valid_before(datetime.date.today())
not_after = builder.not_valid_after(datetime.date.today() + datetime.timedelta(days=365))

# Set the public key of the certificate to be the public key associated with the private key
public_key = private_key.public_key()
builder.public_key(public_key)

# Set the signature algorithm for the certificate
builder.signature_hash_algorithm(cryptography.hazmat.primitives.hashes.SHA256())

# Build the X.509 certificate
certificate = builder.build(private_key=private_key)

# Write the certificate to a file in DER format
with open("my_certificate.der", "wb") as f:
    f.write(cryptography.x509.Certificate.load(certificate).dump())
