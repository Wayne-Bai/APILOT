from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import pkcs7

def deserialize_der_pkcs7_to_certificates(der_data):
    """
    Deserialize a DER encoded PKCS7 blob to a list of certificates.

    :param der_data: DER encoded PKCS7 data
    :return: List of certificates
    """
    pkcs7_object = pkcs7.load_der_pkcs7_certificates(der_data, backend=default_backend())
    certificates = pkcs7_object.certificates
    return certificates
