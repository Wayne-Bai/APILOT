from cryptography.hazmat.primitives.serialization import pkcs7

def deserialize_der_pkcs7_certificates(der_data):
    """
    Deserialize a DER-encoded PKCS7 blob to a list of certificates.
    
    :param der_data: bytes of the DER-encoded PKCS7
    :return: List of certificates found in the PKCS7 structure
    """
    # Load the PKCS7 data
    pkcs7_structure = pkcs7.load_der_pkcs7_certificates(der_data)
    
    # Retrieve the certificates from the PKCS7 structure
    certificates = pkcs7_structure.certificates
    
    return certificates
