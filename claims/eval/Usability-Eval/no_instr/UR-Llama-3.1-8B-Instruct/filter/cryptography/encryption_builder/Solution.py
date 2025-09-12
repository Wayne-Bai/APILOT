from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class AES_ECB_Builder:
    def __init__(self, key):
        self.key = key
        self.cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())

    def encryptor(self):
        return self.cipher.encryptor()

    def decryptor(self):
        return self.cipher.decryptor()


def generate_aes_ecb_builder(key):
    return AES_ECB_Builder(key)


# Example usage
key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x10\x11\x12\x13\x14\x15'
builder = generate_aes_ecb_builder(key)
encryptor = builder.encryptor()
decryptor = builder.decryptor()

# Note: ECB mode is not recommended for use in production due to its vulnerability to padding attacks.
# For secure encryption, consider using CBC or GCM mode.
