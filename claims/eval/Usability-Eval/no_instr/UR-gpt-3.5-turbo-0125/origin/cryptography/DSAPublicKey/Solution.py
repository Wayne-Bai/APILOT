
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa

private_key = dsa.generate_private_key(key_size=1024, backend=default_backend())
public_key = private_key.public_key()

print(public_key)
