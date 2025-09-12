from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

class EncryptionBuilder:
    def __init__(self):
        self.backend = default_backend()
        self.algorithm = algorithms.AES(key_size=256)
        self.mode = modes.CBC()
        self.padding = padding.PKCS7(algorithms.AES.block_size)

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def set_mode(self, mode):
        self.mode = mode

    def set_padding(self, padding_prop):
        self.padding = padding_prop

    def encrypt(self, plaintext, key):
        iv = os.urandom(self.mode.iv_size)
        cipher = Cipher(self.algorithm, self.mode(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        padded_data = self.padding.pad(plaintext.encode(), self.algorithm.block_size)
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        return iv + ciphertext

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:self.mode.iv_size]
        ciphertext = ciphertext[self.mode.iv_size:]

        cipher = Cipher(self.algorithm, self.mode(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        padded_plaintext = self.padding.unpad(padded_plaintext, self.algorithm.block_size)
        return padded_plaintext.decode()

# Example usage
builder = EncryptionBuilder()
key = os.urandom(32)  # 256-bit key
plaintext = b"Hello, world!"

ciphertext = builder.encrypt(plaintext, key)
print(f"Encrypted: {ciphertext.hex()}")

decrypted_plaintext = builder.decrypt(ciphertext, key)
print(f"Decrypted: {decrypted_plaintext}")
