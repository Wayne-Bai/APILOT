from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_x509_certificate

def deserialize_pkcs7(pkcs7_blob):
    # Load the DER encoded PKCS7 blob
    pkcs7_data = serialization.load_der_pkcs7(pkcs7_blob, default_backend())

    # Extract the certificates from the PKCS7 blob
    certificates = pkcs7_data.serial_number_to_certificate_list()

    # Convert the certificates to PEM format
    pem_certificates = [load_pem_x509_certificate(cert.public_bytes(serialization.Encoding.PEM)) for cert in certificates]

    return pem_certificates
