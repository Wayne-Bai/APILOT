from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import datetime

def get_next_update_datetime(crl_data):
    crl = x509.load_der_x509_crl(crl_data, default_backend())
    next_update = crl.next_update
    return next_update.replace(tzinfo=None)

# Example usage:
# crl_data = b'... binary CRL data ...'
# next_update_datetime = get_next_update_datetime(crl_data)
# print(next_update_datetime)
