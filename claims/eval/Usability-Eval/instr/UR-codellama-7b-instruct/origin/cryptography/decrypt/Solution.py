
import cryptography
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken

# Decrypts a Fernet token and returns the original plaintext
def decrypt_fernet(token: str) -> bytes:
    # Load the secret key from disk or an environment variable
    secret_key = b'YOUR_SECRET_KEY'
    
    # Create a Fernet object with the secret key
    f = Fernet(secret_key)
    
    # Attempt to decrypt the token
    try:
        return f.decrypt(token.encode())
    except InvalidToken:
        raise ValueError('Invalid Fernet token') from None
