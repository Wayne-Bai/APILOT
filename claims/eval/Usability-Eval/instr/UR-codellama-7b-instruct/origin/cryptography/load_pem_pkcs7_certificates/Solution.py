
import cryptography.hazmat.backends
from cryptography.x509 import load_pem_x509_certificates
from cryptography.hazmat.primitives.serialization import Encoding

def deserialize_pem_pkcs7_to_list(pem_data):
    backend = cryptography.hazmat.backends.default_backend()
    pem_file = load_pem_x509_certificates(pem_data, Encoding.PEM)
    return list(pem_file)
