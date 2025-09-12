import cryptography

def decrypt_fernet_token(fernet_token):
    key = b'your_secret_key_here'  # replace with your actual secret key
    fernet = cryptography.fernet.Fernet(key)
    try:
        decrypted_data = fernet.decrypt(fernet_token)
        return decrypted_data.decode('utf-8')
    except cryptography.fernet.InvalidToken:
        raise Exception("Invalid Fernet token")
