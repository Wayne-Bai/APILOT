from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.backends import default_backend

def deserialize_pkcs7(pem_data):
    try:
        pkcs7_objs = load_pem_public_key(pem_data, backend=default_backend())
        certificates = [cert for cert in pkcs7_objs]
        return certificates
    except Exception as e:
        print(f"Error deserializing PKCS7 data: {e}")
        return None
