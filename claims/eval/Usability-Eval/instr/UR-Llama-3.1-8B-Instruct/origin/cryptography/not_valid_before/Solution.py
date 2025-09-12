from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID
from cryptography.x509 import Certificate, load_pem_x509_certificate, load_der_x509_certificate
from cryptography.x509.extensions import ExtensionNotFound
from datetime import datetime
from django.utils import timezone

def get_cert_validity_start_date(pem_cert):
    try:
        # Parse the certificate
        cert = load_pem_x509_certificate(pem_cert, default_backend())
        # Get the not before date
        not_before = cert.not_valid_before
        # Convert the date to a datetime object
        validity_start_date = datetime(not_before.year, not_before.month, not_before.day, tzinfo=timezone.utc)
    except ExtensionNotFound:
        # If the certificate does not have a not before date, return a default value
        validity_start_date = datetime(2000, 1, 1, tzinfo=timezone.utc)
        
    return validity_start_date.isoformat()
