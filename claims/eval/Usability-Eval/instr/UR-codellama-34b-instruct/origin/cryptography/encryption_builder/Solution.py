
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Key and initialization vector for encryption
key = b"a secret key"
iv = b"an initialization vector"

# Create an AES-256 cipher object in CBC mode
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

# Encrypt some data using the cipher object
data = b"some data to encrypt"
encrypted = cipher.encrypt(data)
print(encrypted)

# Decrypt the encrypted data using the same key and initialization vector
decrypted = cipher.decrypt(encrypted)
print(decrypted)
