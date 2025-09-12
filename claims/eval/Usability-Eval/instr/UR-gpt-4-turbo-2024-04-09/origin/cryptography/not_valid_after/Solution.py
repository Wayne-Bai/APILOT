from cryptography import x509
from datetime import datetime, timedelta

# Set the start time of the certificate
start_time = datetime.utcnow()

# Set the end time of the certificate, e.g., 1 year from the start time
end_time = start_time + timedelta(days=365)

# Create an X.509 certificate showing example of validity period
certificate = x509.CertificateBuilder().not_valid_before(start_time).not_valid_after(end_time)
