
import cryptography
from cryptography.x509 import Certificate, RevocationInfo, RevocationReason

# Generate a Naïve DateTime
naive_datetime = datetime.now().replace(tzinfo=None)

# Create a new RevocationInfo object with the revoked date
revocation_info = RevocationInfo(
    reason=RevocationReason.UNSPECIFIED,
    crl_number=12345,
    last_update=naive_datetime
)

# Generate a certificate with the revocation info
certificate = Certificate.generate(revocation_info=revocation_info)

print(certificate.to_pem())
