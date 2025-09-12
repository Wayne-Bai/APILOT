from cryptography import x509
from cryptography.hazmat.backends import default_backend

def deserialize_pkcs7_blob(der_data):
    try:
        p7 = x509.load_der_pkcs7_certificates(der_data, default_backend())

        certificates = p7.certificates if p7 else []
        return certificates

    except ValueError:
        print("Invalid PKCS7 data.")
        return []
    except Exception as e:
        print("Error: ", str(e))
        return []
