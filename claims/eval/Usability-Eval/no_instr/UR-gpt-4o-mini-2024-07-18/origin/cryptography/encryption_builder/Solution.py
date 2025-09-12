from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to encrypt a value
def encrypt_value(value):
    encoded_value = value.encode('utf-8')
    encrypted_value = cipher_suite.encrypt(encoded_value)
    return encrypted_value

# Function to decrypt a value
def decrypt_value(encrypted_value):
    decrypted_value = cipher_suite.decrypt(encrypted_value)
    return decrypted_value.decode('utf-8')

# Example usage
if __name__ == "__main__":
    value_to_encrypt = "Hello, World!"
    encrypted = encrypt_value(value_to_encrypt)
    print(f"Encrypted: {encrypted}")

    decrypted = decrypt_value(encrypted)
    print(f"Decrypted: {decrypted}")
