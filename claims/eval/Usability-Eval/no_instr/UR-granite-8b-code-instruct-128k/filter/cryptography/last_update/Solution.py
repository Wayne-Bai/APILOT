from cryptography import x509
from cryptography.hazmat.backends import default_backend

def get_crl_last_updated(crl_path):
    with open(crl_path, "rb") as crl_file:
        crl_data = crl_file.read()

    crl = x509.load_pem_x509_crl(crl_data, default_backend())
    last_updated = crl.last_updated

    return last_updated
