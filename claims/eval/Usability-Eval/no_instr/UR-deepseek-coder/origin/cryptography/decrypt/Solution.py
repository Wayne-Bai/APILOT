from cryptography.fernet import Fernet

def decrypt_fernet_token(token, key):
    fernet = Fernet(key)
    try:
        plaintext = fernet.decrypt(token)
        return plaintext.decode()
    except Exception as e:
        raise Exception(f"Decryption failed: {e}")

# Example usage:
# key = Fernet.generate_key()
# fernet = Fernet(key)
# token = fernet.encrypt(b"Secret message")
# decrypted_message = decrypt_fernet_token(token, key)
# print(decrypted_message)
