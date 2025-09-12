from cryptography.fernet import Fernet

def generate_key():
    """Generates a secure random key for encryption and decryption."""
    return Fernet.generate_key()

def get_fernet_cipher(key):
    """Returns a Fernet cipher object for encrypting and decrypting data."""
    return Fernet(key)

def encrypt_value(fernet_cipher, value):
    """Encrypts a string value using the provided Fernet cipher."""
    if not isinstance(value, bytes):
        value = value.encode('utf-8')
    encrypted_data = fernet_cipher.encrypt(value)
    return encrypted_data

def decrypt_value(fernet_cipher, encrypted_value):
    """Decrypts an encrypted value using the provided Fernet cipher."""
    decrypted_data = fernet_cipher.decrypt(encrypted_value)
    return decrypted_data.decode('utf-8')

# Example Usage
key = generate_key()
cipher = get_fernet_cipher(key)
encrypted = encrypt_value(cipher, "Hello, World!")
print("Encrypted:", encrypted)
decrypted = decrypt_value(cipher, encrypted)
print("Decrypted:", decrypted)
