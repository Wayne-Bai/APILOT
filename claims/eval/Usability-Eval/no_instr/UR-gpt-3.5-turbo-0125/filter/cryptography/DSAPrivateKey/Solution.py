
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend

private_key = dsa.generate_private_key(key_size=1024, backend=default_backend())
