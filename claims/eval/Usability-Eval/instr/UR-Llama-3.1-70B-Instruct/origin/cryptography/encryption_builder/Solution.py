# Import required libraries
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from enum import Enum
import base64
import os

# Define an enumeration for configuration
class EncryptionConfiguration(Enum):
    AES_128_GCM = 1
    AES_192_GCM = 2
    AES_256_GCM = 3

class EncryptionBuilder:
    def __init__(self, configuration):
        if not isinstance(configuration, EncryptionConfiguration):
            raise ValueError("Invalid configuration")
        self.configuration = configuration
        self.key = None

    def with_password(self, password, salt=None):
        """
        Generate key using password and salt.
        
        Args:
            password (str): Password to generate key from.
            salt (bytes, optional): Salt to use. Defaults to a random salt.
        """
        if salt is None:
            salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        self.key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return self

    def build(self):
        """
        Build an Fernet instance for encryption.
        
        Returns:
            Fernet: Fernet instance with generated key.
        """
        if self.key is None:
            raise ValueError("Key not generated")
        return Fernet(self.key)

# Example usage
if __name__ == "__main__":
    configuration = EncryptionConfiguration.AES_256_GCM
    builder = EncryptionBuilder(configuration)
    fernet = builder.with_password("my_password").build()
    
    # Encrypt data
    encrypted = fernet.encrypt(b"Hello, World!")
    print("Encrypted:", encrypted)
    
    # Decrypt data
    decrypted = fernet.decrypt(encrypted)
    print("Decrypted:", decrypted)
