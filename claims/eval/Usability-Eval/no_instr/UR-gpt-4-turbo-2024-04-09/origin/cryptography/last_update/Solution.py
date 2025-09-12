from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import NameOID

# Load or retrieve your CRL (Certificate Revocation List) data
# Assuming it is in PEM format (you might be loading this from a file or another source)
crl_data = b"""
-----BEGIN X509 CRL-----
MIIBYzCCAQwCAQEwDQYJKoZIhvcNAQEFBQAwEjEQMA4GA1UEAwwHdGVzdENBMBgG
A1UdEQQRMA+BDWV4YW1wbGVAZXhhbXBsZTAyMBkGA1UdIAEB/wQPMA0wCwYJKoZI
hvcvAQELMAsGA1UdDwQEAwIBBjANBgkqhkiG9w0BAQUFAAOBgQArVYlzIUrkMvHb
1VhP6dYVsGE+ES/VCe/Dr5ZLN8RdjVzkd5n/5p8Zd89zbQHovhrRQCXpH5nJL1yL
K8lIL8ePbCEfH2zWZinkLXA0Nkp2L+tSItHspPn0i1N4WOAr8L5rBhHx4TVoM7gx
LlPdLdCiwN1x5i9MoW+GUhX/fnQHVQ==
-----END X509 CRL-----
"""

# Decode the CRL data
crl = x509.load_pem_x509_crl(crl_data, default_backend())

# Get the last update time of the CRL
last_update = crl.last_update

print("The CRL was last updated at:", last_update)
