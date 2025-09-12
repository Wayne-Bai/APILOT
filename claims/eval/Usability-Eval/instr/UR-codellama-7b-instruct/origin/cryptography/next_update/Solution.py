
import cryptography
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.x509.base import RevocationList

def get_next_update(crl: RevocationList):
    """
    A naïve datetime representing when the next update to this CRL is expected.

    Args:
        crl (RevocationList): The CRL to get the next update for.

    Returns:
        datetime: The next update datetime.
    """
    # Get the next update as a float
    next_update = crl.next_update

    # Convert the float to a datetime object
    return next_update.replace(tzinfo=cryptography.x509.utils.UTC)
