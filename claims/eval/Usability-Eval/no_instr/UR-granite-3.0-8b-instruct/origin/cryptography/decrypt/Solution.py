from cryptography.fernet import Fernet, InvalidToken

def decrypt_fernet_token(encrypted_token: str) -> str:
    try:
        key = Fernet.generate_key()  # Replace this with your actual key
        f = Fernet(key)
        decrypted_token = f.decrypt(encrypted_token.encode()).decode()
        return decrypted_token
    except InvalidToken:
        raise Exception("Invalid token. Please provide a valid Fernet token.")
