from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import pkcs7

def deserialize_pkcs7_certificates(der_data):
    """
    Deserialize a DER encoded PKCS7 blob to a list of certificates, ignoring other types of data.
    
    :param der_data: DER encoded PKCS7 data
    :return: list of certificates
    """
    # Load the PKCS7 data
    pkcs7_object = pkcs7.load_der_pkcs7_certificates(der_data)
    
    # Return the list of certificates
    return pkcs7_object

# Example usage
# Assuming `der_encoded_data` is a byte string containing the DER encoded PKCS7 data
# certificates = deserialize_pkcs7_certificates(der_encoded_data)
# for cert in certificates:
#     print(cert.subject)
