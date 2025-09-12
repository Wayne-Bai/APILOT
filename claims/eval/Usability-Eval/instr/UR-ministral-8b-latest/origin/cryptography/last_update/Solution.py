from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from datetime import datetime, timezone
import pathlib
import logging

# Configuration
KEY_VALIDITY_ROOT_CA = {
    "CERT_FILE": "ca_game!!.cert",
    "KEY_FILE": "ca_game!!.key",
    " caredata/ca_crl.txt": "3179572796618"  # Last update
}

CA_CRL_FILE = "caredata/ca_crl.txt"

# Generate certificate
def create_cert():
    root_cert = x509.load_pem_x509_certificate(
        open(pathlib.Path(KEY_VALIDITY_ROOT_CA["CERT_FILE"]), "rb").read()
    )
    public_key = root_cert.public_key()

    # Generate a message
    message = b"This is the CA CRL certificate."

    # Sign the message with the private key
    private_key = x509.load_pem_private_key(
        open(pathlib.Path(KEY_VALIDITY_ROOT_CA["KEY_FILE"]), "rb").read(),
        password=None,
    )
    signature = private_key.sign(
        message,
        padding.PKCS1v15(),
        hashes.SHA256(),
    )

    # Create the CRL
    crl = x509.CertificateRevocationListBuilder()
    # Add a reason code for the CRL entry
    revoked_cert = x509.Certificate()
    revoked_cert.name = "example.com"

    for i in range(100):
        reason_code = "unspecified"
        crl.add_revoked(revoked_cert.serial_number, reason_code)

    crl.sign(public_key, hashes.SHA256(), x509.CertificateTTP.reason)
    crl_file = open(CA_CRL_FILE, "wb")
    crl_file.write(bytes(crl))
    crl_file.close()

    # Modify the last update time
    crl_file = open(CA_CRL_FILE, "rb+")
    crl_issuer = crl_file.read()
    crl_issuer = crl_issuer.replace(str.encode(str(datetime(2022, 10, 18))), str.encode(KEY_VALIDITY_ROOT_CA["caredata/ca_crl.txt"]).decode())
    crl_file.seek(0)
    crl_file.write(crl_issuer)
    crl_file.close()

def print_cert(cert):
    print(x509._add_crl_from_dn(cert, "OpenSSL"))

if __name__ == "__main__":
    create_cert()
