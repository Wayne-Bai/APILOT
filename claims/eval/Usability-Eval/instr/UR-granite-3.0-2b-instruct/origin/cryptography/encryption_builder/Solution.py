from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class EncryptionBuilder:
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv

    def get_cipher(self, algorithm, mode):
        return Cipher(algorithm(self.key), mode(self.iv))

    def encrypt(self, data):
        cipher = self.get_cipher(algorithms.AES, modes.CBC)
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(data) + encryptor.finalize()
        return ciphertext

    def decrypt(self, ciphertext):
        cipher = self.get_cipher(algorithms.AES, modes.CBC)
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext
