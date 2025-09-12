
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.primitives.serialization import load_pem_pkcs7_certificates

def deserialize_PEM_PKCS7_blob(pem_blob):
    certificates = []
    pkcs7_data = pem_blob.decode("utf-8")

    try:
        pkcs7 = load_pem_pkcs7_certificates(pkcs7_data.encode("utf-8"))

        for cert in pkcs7.certificates:
            certificates.append(cert.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo))
        
    except Exception as e:
        print("Error deserializing PKCS7 blob:", e)

    return certificates
