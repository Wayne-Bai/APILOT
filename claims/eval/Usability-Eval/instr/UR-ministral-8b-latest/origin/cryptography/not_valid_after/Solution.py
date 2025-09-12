from cryptography import x509
from cryptography.hazmat.primitives import hashes
from datetime import datetime, timedelta
from cryptography.hazmat.primitives.asymmetric import rsa

# Define the end of validity period
end_of_validity = datetime.utcnow() + timedelta(days=365)  # Example end period, add or subtract days as needed

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Generate a self-signed certificate
cert = x509.CertificateBuilder().subject_name(
    x509.Name([
        x509.NameAttribute(x509.NameOID.COMMON_NAME, "example.com")
    ])
).issuer_name(
    x509.Name([
        x509.NameAttribute(x509.NameOID.COMMON_NAME, "example.com")
    ])
).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    start_period = datetime.utcnow()
).not_valid_after(
    end_period = end_of_validity
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"example.com")]),
    critical=False,
).sign(
    private_key=private_key,
    algorithm=hashes.SHA256()
)

print(cert)
