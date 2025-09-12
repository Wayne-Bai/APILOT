import datetime
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_der_private_key

# Sample private key (replace with your own)
private_key_data = b"""
-----BEGIN RSA PRIVATE KEY-----
<Private Key Here>
-----END RSA PRIVATE KEY-----
"""

# Load the private key
private_key = load_der_private_key(private_key_data, password=None, backend=default_backend())

# Get the next update date
next_update = datetime.datetime.now() + datetime.timedelta(days=30)

# Create a new CRL (Certificate Revocation List)
crl = x509.CertificateRevocationList(
    issuer=x509.Name([
        x509.NameAttribute(x509.NameOID.COMMON_NAME, u"My CA"),
    ]),
    last_update=datetime.datetime.now(),
    next_update=next_update
)

# Sign the CRL with our private key
crl = crl.sign(private_key, hashes.SHA256())

# Write the CRL to a file
with open("my_ca.crl", "wb") as f:
    f.write(crl.public_bytes(x509.Encoding.PEM))
