from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class MyEncryptClass:
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv

    def encrypt_text(self, plaintext):
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv))
        encryptor = cipher.encryptor()
        encrypted = encryptor.update(plaintext) + encryptor.finalize()
        return encrypted

    def decrypt_text(self, encrypted_text):
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv))
        decryptor = cipher.decryptor()
        decrypted = decryptor.update(encrypted_text) + decryptor.finalize()
        return decrypted
