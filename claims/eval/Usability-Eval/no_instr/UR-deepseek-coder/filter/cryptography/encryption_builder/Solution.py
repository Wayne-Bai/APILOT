from cryptography.fernet import Fernet

def configure_encryption_builder():
    # Generate a key for encryption and decryption
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    # Define a function to encrypt data
    def encrypt_data(data):
        return cipher_suite.encrypt(data.encode())

    # Define a function to decrypt data
    def decrypt_data(encrypted_data):
        return cipher_suite.decrypt(encrypted_data).decode()

    # Return the encryption and decryption functions
    return encrypt_data, decrypt_data

# Example usage
encrypt_data, decrypt_data = configure_encryption_builder()

# Encrypt a message
encrypted_message = encrypt_data("Hello, World!")
print(f"Encrypted: {encrypted_message}")

# Decrypt the message
decrypted_message = decrypt_data(encrypted_message)
print(f"Decrypted: {decrypted_message}")
