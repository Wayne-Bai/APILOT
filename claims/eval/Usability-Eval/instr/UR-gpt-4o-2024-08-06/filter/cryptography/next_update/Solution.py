from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import NameOID
from cryptography import x509
from datetime import datetime, timedelta

# Function to create a Certificate Revocation List (CRL)
def create_crl(private_key, revoked_certificates, issuer_name, next_update_days):
    builder = x509.CertificateRevocationListBuilder()
    builder = builder.issuer_name(issuer_name)
    builder = builder.last_update(datetime.utcnow())

    # Set the next update field to the current time plus the provided number of days
    builder = builder.next_update(datetime.utcnow() + timedelta(days=next_update_days))

    # Add revoked certificates to the CRL
    for serial_number, revocation_date in revoked_certificates:
        revoked_certificate = x509.RevokedCertificateBuilder().serial_number(
            serial_number
        ).revocation_date(
            revocation_date
        ).build()
        builder = builder.add_revoked_certificate(revoked_certificate)

    # Sign the CRL with the private key
    crl = builder.sign(private_key=private_key, algorithm=hashes.SHA256())
    return crl

# Example usage
issuer_name = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Organization"),
    x509.NameAttribute(NameOID.COMMON_NAME, "My Common Name"),
])

# Generate a private key for signing the CRL (for example purposes)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

revoked_certificates = [
    (123456789, datetime.utcnow()),
    (987654321, datetime.utcnow())
]

crl = create_crl(private_key, revoked_certificates, issuer_name, next_update_days=30)

# Serialize CRL to PEM format for storage or distribution
crl_pem = crl.public_bytes(serialization.Encoding.PEM)
print(crl_pem.decode())
