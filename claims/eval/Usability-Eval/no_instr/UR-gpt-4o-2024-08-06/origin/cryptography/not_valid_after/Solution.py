from cryptography import x509
from cryptography.hazmat.backends import default_backend
import datetime

# Define the end validity datetime in UTC
end_validity_datetime = datetime.datetime.utcnow()

# Create a certificate with a validity that is inclusive of end_validity_datetime
certificate_builder = x509.CertificateBuilder()

# (The rest of the required certificate fields such as subject_name, issuer_name, public_key, etc. should be added here)

# Set the validity period of the certificate
certificate_builder = certificate_builder.not_valid_before(datetime.datetime.utcnow())  # Typically the current UTC time
certificate_builder = certificate_builder.not_valid_after(end_validity_datetime)  # The inclusive end validity period

# Generate the certificate
# (Assume private_key is defined and valid)
#certificate = certificate_builder.sign(private_key=private_key, algorithm=hashes.SHA256(), backend=default_backend())

# Now you have a certificate with the specified validity period
