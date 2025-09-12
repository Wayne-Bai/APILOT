from cryptography.x509 import Certificate
from datetime import datetime, timedelta

# Define function to get the end of the validity period
def get_certificate_validity_end(certificate: Certificate) -> datetime:
    # Get the not_valid_after attribute from the certificate
    not_valid_after = certificate.not_valid_after
    # Convert to naive datetime (UTC)
    return not_valid_after.replace(tzinfo=None)

# Example usage: assuming `cert` is an instance of Certificate
# cert = ... (Load or create your certificate)
# validity_end = get_certificate_validity_end(cert)
# print(validity_end)
