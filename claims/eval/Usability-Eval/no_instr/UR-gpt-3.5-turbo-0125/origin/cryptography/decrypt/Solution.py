
from cryptography.fernet import Fernet

def decrypt_fernet_token(token, key):
    f = Fernet(key)

    try:
        decrypted_data = f.decrypt(token)
    except InvalidToken:
        raise Exception("Invalid token. Could not decrypt.")
    
    return decrypted_data

# Example usage
token = b'...'
key = b'...'
result = decrypt_fernet_token(token, key)
print(result.decode())
