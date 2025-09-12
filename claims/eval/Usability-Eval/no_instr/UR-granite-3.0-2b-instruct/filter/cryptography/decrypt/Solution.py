from cryptography.fernet import Fernet

def decrypt_token(token, key):
    try:
        fernet = Fernet(key)
        decrypted_token = fernet.decrypt(token)
        return decrypted_token.decode('utf-8')
    except Exception as e:
        raise Exception("Invalid token or key") from e
