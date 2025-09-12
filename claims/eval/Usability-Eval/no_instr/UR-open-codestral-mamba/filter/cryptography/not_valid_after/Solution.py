from cryptography import x509
from cryptography.hazmat.backends import default_backend
import datetime

# Create a self-signed certificate with a serial number, subject name, public key, and validity period
def generate_self_signed_certificate(key, public_key, subject, issuer, serial, validity_days, signature_algorithm):
    # Set the certificate validity period
    not_valid_before = datetime.datetime.utcnow()
    not_valid_after = datetime.datetime.utcnow() + datetime.timedelta(days=validity_days)

    # Create the certificate
    builder = x509.CertificateBuilder()
    builder = builder.subject_name(subject)
    builder = builder.issuer_name(issuer)
    builder = builder.serial_number(serial)
    builder = builder.public_key(public_key)
    builder = builder.not_valid_before(not_valid_before)
    builder = builder.not_valid_after(not_valid_after)
    builder = builder.add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)

    # Sign the certificate with the given key
    certificate = builder.sign(key, signature_algorithm, default_backend())

    return certificate

# Usage example
key = x509.generate_private_key(x509.oid.RSA_SHA256(), default_backend())
public_key = key.public_key()
subject = x509.Name([x509.NameAttribute(x509.oid.NameOID.COMMON_NAME, u"My Server")])
issuer = subject
serial = x509.random_serial_number()
validity_days = 365
signature_algorithm = x509.oid.RSA_SHA256

certificate = generate_self_signed_certificate(key, public_key, subject, issuer, serial, validity_days, signature_algorithm)

# Save the certificate to a file
with open('my_cert.pem', 'wb') as f:
    f.write(certificate.public_bytes(x509.Encoding.PEM))
