
from cryptography.fernet import Fernet

class EncryptionType:
    AES = 1
    RSA = 2

    def get_encrypt_builder(self, encryption_type):
        if encryption_type == EncryptionType.AES:
            key = Fernet.generate_key()
            cipher = Fernet(key)
            return cipher
        elif encryption_type == EncryptionType.RSA:
            # Add RSA encryption logic here
            pass
        else:
            print("Invalid encryption type")

# Example usage:
encryption_type = EncryptionType.AES
encrypt_builder = encryption_type.get_encrypt_builder(encryption_type)
print(encrypt_builder)
