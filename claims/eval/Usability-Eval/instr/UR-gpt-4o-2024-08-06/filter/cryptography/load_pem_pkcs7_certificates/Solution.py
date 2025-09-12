from cryptography.hazmat.primitives.serialization import pkcs7
from cryptography.hazmat.backends import default_backend

def deserialize_pem_pkcs7_certs(pkcs7_data: bytes):
    """
    Deserialize a PEM encoded PKCS7 blob to a list of certificates.
    This function extracts and returns only the certificates from the PKCS7 structure.
    
    :param pkcs7_data: The PKCS7 blob in PEM format as bytes.
    :return: List of certificates found in PKCS7 structure.
    """
    # Load the PKCS7 data
    pkcs7_obj = pkcs7.load_pem_pkcs7_certificates(pkcs7_data, backend=default_backend())
    
    # Extract and return certificates from PKCS7 object
    return pkcs7_obj

# Example usage
# Assuming `pem_pkcs7_blob` is a variable containing the PEM PKCS7 blob as bytes
# certificates = deserialize_pem_pkcs7_certs(pem_pkcs7_blob)
# for cert in certificates:
#     print(cert.subject)
