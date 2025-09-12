from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509 import CertificateBuilder, NameConstraints

# Generate a private key
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Generate the certificate
builder = CertificateBuilder()
builder = builder.subject_name(NameConstraints([], [])).issuer_name(NameConstraints([], []))
cert = builder.build(private_key)

# Serialize the certificate to a file
with open('cert.crt', 'wb') as f:
    f.write(serialization.Encoding.PEM.encode(cert, format=serialization.Format.DER))
