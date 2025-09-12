from cryptography import x509

def deserialize_pkcs7_blob(blob):
    # Initialize a reader to parse the DER encoded PKCS7 blob
    parser = x509.PKCS7.parse_der(blob)

    # Extract the Certificates from the PKCS7 contents
    certificates = list(parser.certificates)

    return certificates
