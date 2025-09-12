from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, dsakey, ec

def deserialize_private_key(ssh_data, password=None):
    private_key = serialization.load_ssh_private_key(
        ssh_data, password=password, backend=default_backend()
    )

    if isinstance(private_key, rsa.RSAPrivateKey):
        print("The private key is an RSA key.")
    elif isinstance(private_key, dsa.DSAPrivateKey):
        print("The private key is a DSA key.")
    elif isinstance(private_key, ec.EllipticCurvePrivateKey):
        print("The private key is an elliptic curve key.")

    return private_key
