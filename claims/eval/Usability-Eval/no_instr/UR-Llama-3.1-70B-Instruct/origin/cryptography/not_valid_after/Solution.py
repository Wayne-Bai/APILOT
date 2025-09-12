from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta
import os

def generate_self_signed_cert():
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    name = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, u"桜MainActivity"),
    ])

    alt_name = x509.SubjectAlternativeName([
            x509.DNSName(u"localhost"),
    ])

    cert = (
        x509.CertificateBuilder()
       .subject_name(name)
       .issuer_name(name)
       .public_key(key.public_key())
       .serial_number(x509.random_serial_number())
       .not_valid_before(datetime.utcnow())
       .not_valid_after(datetime.utcnow() + timedelta(days=30)) # End of validity period
       .add_extension(alt_name, critical=False)
       .sign(key, hashes.SHA256())
    )

    return cert

cert = generate_self_signed_cert()
print("Validity End: ", cert.not_valid_after)
