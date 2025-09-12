from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import ExtensionOID
import datetime

# Example PEM encoded certificate (replace with actual certificate)
pem_data = b"""
-----BEGIN CERTIFICATE-----
MIIC+DCCAeCgAwIBAgIJAN8k9K7T7OlDMA0GCSqGSIb3DQEBCwUAMBoxGDAWBgNV
BAMMD3d3dy5leGFtcGxlLmNvbTAeFw0xOTA2MTIwNzMwNDNaFw0yOTA2MDkwNzMw
...
-----END CERTIFICATE-----
"""

# Load the certificate
certificate = x509.load_pem_x509_certificate(pem_data, default_backend())

# Check if the certificate has the revocation date extension
try:
    # Get the CRL Distribution Points extension from the certificate
    crl_distribution_points = certificate.extensions.get_extension_for_oid(
        ExtensionOID.CRL_DISTRIBUTION_POINTS
    ).value

    # For demonstration, we'll assume the first CRL distribution point is relevant
    crl_url = crl_distribution_points[0].full_name[0].value

    # Consider the CRL URL as a place to fetch a CRL and determine the revocation date
    # Since we cannot fetch a CRL in this setup, we'll demonstrate with a fake date
    revocation_date = datetime.datetime(2023, 1, 1)
    print("Revocation date:", revocation_date)

except x509.ExtensionNotFound:
    print("CRL Distribution Points extension not found in the certificate.")
