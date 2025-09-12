import datetime
from cryptography import x509

# Parse the CRL data
def parse_crl(crl_data):
    crl = x509.load_der_x509_crl(crl_data)

    # Parse the date of last update
    last_update_date = crl.last_update

    return last_update_date

# Test the function
crl_data = b'...'  # Replace '...' with the actual CRL data in DER format
last_update_date = parse_crl(crl_data)

print('Last Update Date:', last_update_date)
