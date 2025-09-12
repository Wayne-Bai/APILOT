
import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import NameOID

# Define the validity period of the certificate in UTC
begin_validity = datetime(2023, 1, 1) # January 1, 2023
end_validity = begin_validity + timedelta(days=90) # plus 90 days

# Define the X.509 certificate builder with the validity period set
builder = serialization.load_pem_x509_certificate(bytes, backend=cryptography.hazmat.backends.default_backend())
builder = builder.serialization
builder.set_not_before(begin_validity)
builder.set_not_after(end_validity)

# Generate the X.509 certificate with the defined validity period
certificate = builder.sign(private_key, algorithm=hashes.SHA256(), backend=cryptography.hazmat.backends.default_backend())
