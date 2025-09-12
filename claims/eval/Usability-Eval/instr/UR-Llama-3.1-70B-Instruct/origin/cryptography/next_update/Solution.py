from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from datetime import datetime, timedelta

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Create certificate subject
subject = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u'CRL Example'),
])

# Create certificate issuer
issuer = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u'CRL Example'),
])

# Set certificate build parameters
cert_build_params = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
)

# Calculate next update to CRL (days until next update)
days_until_next_update = 30

# Calculate next update datetime
next_update_datetime = datetime.now() + timedelta(days=days_until_next_update)

# Set next update to CRL
cert_build_params = cert_build_params.add_extension(
    x509.CRLDistributionPoints([
        x509.DistributionPoint(
            full_name=[
                x509.UniformResourceIdentifier('http://example.com/crl'),
            ],
            relative_name=None,
            reason=None,
            crlIssuer=None,
        ),
    ]),
    critical=False,
)

# Generate certificate
cert = cert_build_params.public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.now()
).not_valid_after(
    datetime.now() + timedelta(days=days_until_next_update)
).sign(private_key, hashes.SHA256(), default_backend())

# Generate CRL (Certificate Revocation List)
crl = x509.CertificateRevocationListBuilder().issuer_name(
    issuer
).last_update(
    datetime.now()
).next_update(
    next_update_datetime
).sign(private_key, hashes.SHA256(), default_backend())

# Print result
print("Next Update:", next_update_datetime)
print("CRL to DER format:", crl.public_bytes(serialization.Encoding.DER).hex())
