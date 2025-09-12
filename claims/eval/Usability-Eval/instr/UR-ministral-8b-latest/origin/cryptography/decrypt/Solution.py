from cryptography.fernet import Fernet

def decrypt_fernet_token(token: bytes, key: bytes) -> str:
    try:
        cipher_suite = Fernet(key)
        decrypted_text = cipher_suite.decrypt(token)
        return decrypted_text.decode()
    except Exception as e:
        raise ValueError("Failed to decrypt the token") from e

# Example usage:
encrypted_token = Fernet.generate_key().hex().encode() + encoded_message
key = Fernet.generate_key().hex().encode()

decrypted_message = decrypt_fernet_token(encrypted_token, key)
print(decrypted_message)
