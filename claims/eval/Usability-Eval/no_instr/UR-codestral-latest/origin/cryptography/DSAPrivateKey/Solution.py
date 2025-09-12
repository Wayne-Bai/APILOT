from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

# Generate a new DSA private key
private_key = dsa.generate_private_key(
    key_size=1024,
    backend=default_backend()
)

# You can save the private_key to a file or use it directly. Here is how you can get the private number as a string.
private_num = private_key.private_numbers().x.decode('utf-8')
print(f'Private number: {private_num}')
