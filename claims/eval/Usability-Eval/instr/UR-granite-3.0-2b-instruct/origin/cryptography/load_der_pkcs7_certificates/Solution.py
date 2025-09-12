from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def deserialize_pkcs7(der_encoded_blob):
    # Load the DER encoded PKCS7 blob
    pkcs7 = serialization.load_pem(der_encoded_blob, default_backend())

    # Get the content type from the PKCS7 header
    content_type = pkcs7.content_type

    # Get the content from the PKCS7 blob
    content = pkcs7.get_content()

    # Initialize an empty list to store the certificates
    certificates = []

    # Iterate over the content objects in the PKCS7 blob
    for content_object in content:
        # Check if the content object is a certificate
        if content_object.tag == 16:
            # Decode the certificate from DER format
            certificate = x509.load_pem_x509_certificate(content_object.get_bytes(), default_backend())

            # Add the certificate to the list
            certificates.append(certificate)

    return certificates
