# Importing the cryptography library
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

class EncryptionFormat:
    def __init__(self, password):
        self.password = password

    def generate_key(self):
        # Generate a key using a password-based key derivation function
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'salt',
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.password.encode()))
        return key

    def encrypt(self, value):
        # Generate a key
        key = self.generate_key()
        # Create a Fernet instance with the key
        fernet = Fernet(key)
        # Encrypt the value
        encrypted_value = fernet.encrypt(value.encode())
        return encrypted_value

    def decrypt(self, encrypted_value):
        # Generate a key
        key = self.generate_key()
        # Create a Fernet instance with the key
        fernet = Fernet(key)
        # Decrypt the value
        value = fernet.decrypt(encrypted_value)
        return value.decode()

# Usage
format = EncryptionFormat("mysecretpassword")
encrypted_value = format.encrypt("Hello, World!")
print(encrypted_value)

decrypted_value = format.decrypt(encrypted_value)
print(decrypted_value)
