from cryptography import x509
from cryptography.hazmat.backends import default_backend

def get_crl_last_update(crl_data):
    """
    Parses the CRL data to find the last update time.

    :param crl_data: byte string containing the CRL data
    :return: datetime object representing the last update of the CRL
    """
    # Load the CRL
    crl = x509.load_der_x509_crl(crl_data, default_backend())

    # Get the last update time
    last_update = crl.last_update

    return last_update

# Example: reading CRL data (assuming it's in DER format)
crl_data = b'Your CRL data here in binary form'
last_update = get_crl_last_update(crl_data)
print("CRL was last updated on:", last_update)
