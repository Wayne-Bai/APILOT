from cryptography.fernet import Fernet

def decrypt_token(encrypted_token, key):
    try:
        f = Fernet(key)
        decrypted_token = f.decrypt(encrypted_token)
        return decrypted_token.decode()
    except Exception as e:
        raise Exception("Failed to decrypt the token") from e
