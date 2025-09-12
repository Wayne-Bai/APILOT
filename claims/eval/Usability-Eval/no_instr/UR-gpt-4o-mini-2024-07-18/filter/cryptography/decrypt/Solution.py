from cryptography.fernet import Fernet

def decrypt_fernet_token(token: bytes, key: bytes) -> bytes:
    fernet = Fernet(key)
    try:
        decrypted_data = fernet.decrypt(token)
        return decrypted_data
    except Exception as e:
        raise ValueError("Decryption failed") from e

# Example usage:
# key = Fernet.generate_key()  # Use a valid key that matches the one used for encryption
# token = b'your_encrypted_token_here'  # Replace with your actual token
# plaintext = decrypt_fernet_token(token, key)
# print(plaintext)
