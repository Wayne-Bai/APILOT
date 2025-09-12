from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import pkcs7

def deserialize_pem_pkcs7(pem_data):
    """
    Deserialize a PEM encoded PKCS7 blob to a list of certificates.

    Args:
    pem_data (bytes): A PEM encoded PKCS7 blob.

    Returns:
    list: A list of x509 certificates.
    """

    # Load the PEM encoded PKCS7 blob
    try:
        pkcs7_data = serialization.pkcs7.PemGetter().parse(pem_data)
    except ValueError as e:
        # If PEM data is malformed or not a PKCS7 blob, return empty list
        print(f"Error parsing PEM data: {e}")
        return []

    # Get the loaded PKCS7 object
    pkcs7_object = pkcs7.load_der_pkcs7_bytearray(pkcs7_data)

    # Initialize an empty list to store the certificates
    certificates = []

    # Iterate over the content of the PKCS7 object
    if pkcs7_object.content:
        if pkcs7_object.content_type == pkcs7.PKCS7_SIGNED:
            # If the PKCS7 object is a signed message, extract the certificates from the signers
            for signer in pkcs7_object.signers:
                certificates.extend(signer.get_underlying_certificates())

    return certificates

# Usage example
if __name__ == "__main__":
    pem_data = b"""-----BEGIN PKCS7-----
   _MIICljCCAc...many lines of base64 encoded data...
    -----END PKCS7-----"""

    certificates = deserialize_pem_pkcs7(pem_data)

    for cert in certificates:
        print(x509.DistinguishedName(cert.subject).get_attributes_for_oid(x509.oid.NameOID.COMMON_NAME))
