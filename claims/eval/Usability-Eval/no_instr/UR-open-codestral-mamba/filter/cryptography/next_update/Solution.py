import datetime
from cryptography.x509 import load_pem_x509_crl
from cryptography.hazmat.backends import default_backend

def get_next_crl_update(crl_file_path):
    with open(crl_file_path, "rb") as file:
        crl_bytes = file.read()

    crl = load_pem_x509_crl(crl_bytes, default_backend())
    next_update = crl.next_update

    return next_update

# Example usage
crl_file_path = "path_to_your_crl_file"
next_update = get_next_crl_update(crl_file_path)
print(next_update)
