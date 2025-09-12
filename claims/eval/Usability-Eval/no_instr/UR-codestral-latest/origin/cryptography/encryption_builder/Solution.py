from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Generate a random 256-bit key and 16-bit IV
key = os.urandom(32)
iv = os.urandom(16)

# Create a cipher object using the AES algorithm with a CBC mode
cipher_config = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

def encrypt(plaintext, cipher):
    # Encrypt the plaintext
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

def decrypt(ciphertext, cipher):
    # Decrypt the ciphertext
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()
    return plaintext

# Test the encryption and decryption
message = b"This is a secret message."
encrypted_message = encrypt(message, cipher_config)
decrypted_message = decrypt(encrypted_message, cipher_config)

# Check if the decrypted message matches the original message
assert message == decrypted_message, "Decrypted message does not match the original message"
