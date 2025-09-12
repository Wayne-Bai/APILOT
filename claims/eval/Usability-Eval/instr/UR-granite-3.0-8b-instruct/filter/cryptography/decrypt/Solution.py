from cryptography.fernet import Fernet, InvalidToken

def decrypt_token(token, key):
    try:
        f = Fernet(key)
        decrypted_token = f.decrypt(token)
        return decrypted_token
    except InvalidToken:
        raise Exception("Invalid token")
