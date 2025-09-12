from cryptography.fernet import Fernet

def decrypt_fernet_token(token, key):
    f = Fernet(key)
    try:
        plaintext = f.decrypt(token)
        return plaintext
    except Exception as e:
        raise e
