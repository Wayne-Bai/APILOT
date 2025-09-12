import cryptography

def deserialize_pem_to_certificates(pem_data):
    """Deserialize a PEM encoded PKCS7 blob to a list of certificates.

    Args:
        pem_data (bytes): The PEM encoded PKCS7 blob to deserialize.

    Returns:
        list[cryptography.x509.Certificate]: A list of deserialized certificates.

    """
    pkcs7 = cryptography.util. serialization.load_pem_object(pem_data)
    if not isinstance(pkcs7, cryptography.hazmat.primitives.serialization.PKCS7):
        raise ValueError("Input data is not a valid PKCS7 object.")
    certificates = []
    for obj in pkcs7.contents:
        if isinstance(obj, cryptography.x509.Certificate):
            certificates.append(obj)

    return certificates
