
import cryptography
from cryptography import x509

def deserialize_pkcs7(pem_data):
    pkcs7 = cryptography.hazmat.primitives.asymmetric.pkcs7.load_pem_pkcs7(
        pem_data,
        cryptography.hazmat.primitives.serialization.Encoding.PEM
    )

    return [x509.Certificate.from_der(cert) for cert in pkcs7.get_raw_bytes()]
