from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()

# Create a new Fernet instance with the generated key
cipher_suite = Fernet(key)

def encrypt_message(message: str) -> str:
    # Convert the message to bytes
    message_bytes = message.encode()

    # Encrypt the message
    encrypted_message = cipher_suite.encrypt(message_bytes)

    # Return the encrypted message
    return encrypted_message.decode()

def decrypt_message(encrypted_message: str) -> str:
    # Convert the encrypted message to bytes
    encrypted_message_bytes = encrypted_message.encode()

    # Decrypt the message
    decrypted_message = cipher_suite.decrypt(encrypted_message_bytes)

    # Return the decrypted message
    return decrypted_message.decode()

# Test the functions by encrypting and then decrypting a message
original_message = 'Hello, World!'
encrypted_message = encrypt_message(original_message)
decrypted_message = decrypt_message(encrypted_message)

original_message, encrypted_message, decrypted_message
