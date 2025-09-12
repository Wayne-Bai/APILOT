import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.x509.ocsp import OCSPRequestBuilder, OCSPResponseBuilder

def get_crl_last_updated(crl):
    """
    Returns a naïve datetime representing when the CRL was last updated.

    :param crl: The Certificate Revocation List (CRL) as a string or bytes.
    :return: A datetime object representing the last update time of the CRL.
    """
    backend = default_backend()
    ocsp_request = OCSPRequestBuilder().read(crl, backend).build(backend)
    ocsp_response = OCSPResponseBuilder().read(ocsp_request, backend).build(backend)
    basic_ocsp_response = ocsp_response.basic_ocsp_response
    last_update = datetime.datetime.strptime(
        basic_ocsp_response.this_update, "%Y-%m-%dT%H:%M:%S"
    )
    return last_update
