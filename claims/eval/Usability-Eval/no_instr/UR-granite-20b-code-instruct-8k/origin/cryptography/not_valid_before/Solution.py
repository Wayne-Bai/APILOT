from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import NameOID

# Generate a naive datetime representing the beginning of the validity period for the certificate in UTC.
start_date = x509.random_serial_number()

# Build the certificate
cert = x509.CertificateBuilder().subject_name(x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u"Some Common Name"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Some Organization"),
])).issuer_name(x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u"Some Common Name"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Some Organization"),
])).public_key(key).serial_number(x509.random_serial_number()).not_valid_before(start_date).not_valid_after(start_date + datetime.timedelta(days=365)).add_extension(
    x509.SubjectAlternativeName([
        x509.DNSName(u"some.dns.name"),
        x509.DNSName(u"anothersome.dns.name"),
        x509.RFC822Name(u"some@email.address"),
    ]), False).sign(key, hashes.SHA256(), default_backend())
