
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encryption_builder(enum_element):
    key = b'YOUR_SECRET_KEY' # 16, 24, or 32 bytes key for AES
    nonce = b'YOUR_NONCE'    # 16 bytes nonce for AES-GCM

    def encrypt_data(data):
        padder = PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()

        cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
        encryptor = cipher.encryptor()

        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return ciphertext

    def decrypt_data(ciphertext):
        cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
        decryptor = cipher.decryptor()

        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = PKCS7(128).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()
        return data

    return encrypt_data, decrypt_data

# Example usage:
# enum_element = ENUM_CONSTANT  # Use your actual enum element here
# encrypt_data, decrypt_data = encryption_builder(enum_element)

# encrypted_data = encrypt_data(b'Hello, World!')
# decrypted_data = decrypt_data(encrypted_data)

