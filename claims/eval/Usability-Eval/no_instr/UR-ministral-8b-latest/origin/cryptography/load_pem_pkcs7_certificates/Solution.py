from cryptography import x509
from cryptography.hazmat.backends import default_backend

def deserialize_pkcs7_blob_to_certificates(pem_blob: str) -> list[x509.Certificate]:
    # Parsing the PEM-encoded PKCS#7 data
    pkcs7_blob = pem_blob.replace('\n', b'\n')

    with open("pkcs7_pem_bin.pem", "wb") as f:
        f.write(pkcs7_blob)

    # Load the PKCS#7 object from the binary file
    pkcs7_data = x509.load_pkcs7_object_of_pems(
        pkcs7_pem_pibs={"certificates": "pkcs7_pem_bin.pem"},
        backend=default_backend(),
    )

    # Extracting the list of certificates
    certificates = []
    for cert_info in pkcs7_data.get_content_info():
        if cert_info.content_type == 9:  # 'Signature'
            continue
        if cert_info.content_type == 4:  # TRUSTED_TLS_CERT
            cert = x509.load_pem_x509_certificate(
                cert_info.content, backend=default_backend()
            )
            certificates.append(cert)

    return certificates

# Example usage
pem_blob = """-----BEGIN PKCS7-----\n...
-----END PKCS7-----"""

certificates = deserialize_pkcs7_blob_to_certificates(pem_blob)
for cert in certificates:
    print(cert.fingerprint())
