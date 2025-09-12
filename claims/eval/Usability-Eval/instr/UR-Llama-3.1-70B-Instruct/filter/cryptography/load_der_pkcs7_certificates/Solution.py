# Import necessary modules
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.pkcs7 import PKCS7, PKCS7Signature
from cryptography.exceptions import UnsupportedAlgorithm

def deserialize_pkcs7(blob: bytes) -> list[x509.BaseCertificate]:
    """
    Deserialize a DER encoded PKCS7 blob to a list of certificates.
    
    Args:
    blob: DER encoded PKCS7 blob
    
    Returns:
    A list of certificates.
    """

    try:
        # Load the PKCS7 blob
        pkcs7 = PKCS7.load_der(blob)

        # Initialize an empty list to store certificates
        certificates = []

        # Iterate over all objects in the PKCS7 blob
        for obj in pkcs7.content:
            try:
                # Attempt to load the object as a certificate
                cert = x509.load_der_x509_certificate(obj.as_bytes())
                certificates.append(cert)
            except ValueError:
                # Ignore non-certificate objects
                continue
            except UnsupportedAlgorithm as e:
                print(f"Unsupported algorithm: {e}")
                continue

        return certificates
    
    except Exception as e:
        print(f"Error: {e}")
        return []

# Example usage:
if __name__ == "__main__":
    # Replace 'pkcs7_blob.der' with your own DER encoded PKCS7 blob file
    with open('pkcs7_blob.der', 'rb') as f:
        blob = f.read()

    certificates = deserialize_pkcs7(blob)

    for cert in certificates:
        print(f"Certificate subject: {cert.subject}")
        print(f"Certificate issuer: {cert.issuer}\n")
