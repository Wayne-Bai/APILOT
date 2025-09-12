from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_public_key

def deserialize_openssh_public_key(data):
    pem_header = "-----BEGIN PUBLIC KEY-----\n"
    pem_footer = "\n-----END PUBLIC KEY-----"

    if not data.startswith(pem_header) or not data.endswith(pem_footer):
        raise ValueError("Invalid PEM data format")

    pem_data = data[len(pem_header):-len(pem_footer)]
    return load_pem_public_key(bytes(pem_data, 'ascii'))

# Example usage:
openssh_data = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxwAG9qScjSuPvOfb3zEO
74chioh1FtIeKc54FTjzoKQCF3njj8vFAm/7MEe+
z6NKhldUmF1Ys denotesKcntc81xzZJvE+YNuiJtKqp+eLItQu4cAFCeU7O3j2N65JZ
-----END PUBLIC KEY-----"""

public_key = deserialize_openssh_public_key(openssh_data)
print(public_key)
