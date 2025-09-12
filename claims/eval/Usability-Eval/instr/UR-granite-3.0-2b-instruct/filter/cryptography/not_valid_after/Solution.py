from datetime import datetime, timedelta
from cryptography import x509

# Define the end of the validity period in UTC
end_of_validity = datetime.utcnow() + timedelta(days=365)

# Create a new certificate with the defined end of validity period
certificate = x509.CertificateBuilder().subject_name(x509.Name([x509.NameAttribute(name="CN", value="example.com")])).not_valid_before(datetime.utcnow()).not_valid_after(end_of_validity).sign(x509.privatekey.PrivateKey.from_private_bytes(b""), hash_algorithm=x509.hash_algorithm.SHA256())

# Print the certificate
print(certificate.public_bytes(encoding=x509.Encoding.PEM))
