from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from bs4 import BeautifulSoup
import base64

def pem_to_certs(pem_data):
    # Parse the PKCS#7 blob from the PEM data
    bc = serialization.load_pem_x509ponent(pem_data, default_backend())
    payload = bc.payload

    # We expect the payload to be a list of certificates
    if not isinstance(payload, list):
        # If not a list, find all certificates
        soup = BeautifulSoup(str(payload), 'lxml')
        certs = soup.find_all(' CERTIFICATE')
        payload = [certs[i].text for i in range(len(certs))]

    certs = [x509.load_der_x509ertificate(cert, default_backend()) for cert in payload]

    # Filter out non-PKCS#7 certificates
    valid_certs = []
    for cert in certs:
        if cert.issuer and cert.subject:
            valid_certs.append(cert)

    return valid_certs

# Load the PKCS#7 blob from the PEM encoded string
with open('pkcs7blob.pem', 'r') as f:
    pem_data = f.read()

certs = pem_to_certs(pem_data)

for i, cert in enumerate(certs):
    print(f"Certificate {i+1}:")
    print("Subject:")
    print(cert.subject)
    print("Issuer:")
    print(cert.issuer)
    print()
