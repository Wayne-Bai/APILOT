from cryptography.hazmat.backends import default_backend
from cryptography import x509

def get_crl_last_update(crl_path):
    with open(crl_path, "rb") as file:
        crl_data = file.read()

    crl = x509.load_der_x509_crl(crl_data, default_backend())
    return crl.last_update

# usage
crl_last_update_time = get_crl_last_update('path_to_your_crl_file')
print('The last update time of the CRL is: ', crl_last_update_time)
