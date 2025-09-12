from cryptography import x509
from cryptography.x509 import CertificateRevocationList, Extension, ExtensionNotFound
from cryptography.x509.revocation import ASN1CRLReason, RevokedCertificate
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.hashes import SHA1, SHA256
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime

# Change these values to fit your needs
key_size = 2048
reason = "cessationOfOperation" # one of: unspecified, keyCompromise, CACompromise, affiliationChanged, superseded, cessationOfOperation, certificateHold, removeFromCRL, privilegeWithdrawn, aACompromise

# Generate the CA private key
ca_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=key_size
)

# Create a self-signed CA certificate
ca_cert = x509.CertificateBuilder().subject_name(x509.Name([
    x509.NameAttribute(x509.NameOID.COMMON_NAME, u"My CA"),
])).issuer_name(x509.Name([
    x509.NameAttribute(x509.NameOID.COMMON_NAME, u"My CA"),
])).state_or_province_name(u"Some-State").country_name(u"US").serial_number(x509.random_serial_number()).public_key(ca_private_key.public_key()).not_valid_before(datetime.utcnow()).not_valid_after(datetime.utcnow() + timedelta(days=365)).add_extension(x509.SubjectKeyIdentifier.from_public_key(ca_private_key.public_key()), critical=False).add_extension(x509.AuthorityKeyIdentifier.from_issuer_public_key(ca_private_key.public_key()), critical=False).add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True).sign(private_key=ca_private_key, algorithm=SHA256())

revoked_cert = RevokedCertificate(
    user_certificate=x509.load_pem_x509_certificate(open("my_cert.pem", "rb").read()),
    revocation_date=datetime.utcnow(),
    crl_reason=getattr(ASN1CRLReason, reason),
)

crl = CertificateRevocationList(
    issuer=ca_cert.subject,
    last_update=datetime.utcnow(),
    next_update=datetime.utcnow() + timedelta(days=30),
    revoked_certificates=[revoked_cert]
)

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=key_size
)

crl_bytes = crl.sign(private_key=private_key, algorithm=SHA1())

with open("revoked.crl", "wb") as f:
    f.write(crl_bytes)
