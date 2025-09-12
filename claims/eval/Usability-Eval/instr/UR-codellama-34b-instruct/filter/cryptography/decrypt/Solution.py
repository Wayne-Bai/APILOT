import base64
from cryptography.fernet import Fernet

def decrypt_token(token):
    """
    Decrypts a Fernet token and returns the original plaintext.
    
    :param token: The Fernet token to decrypt.
    :return: The decrypted plaintext.
    """
    # Load the Fernet key
    fernet_key = Fernet.generate_key()

    # Decrypt the token using the key
    try:
        decrypted_data = Fernet.decrypt(token, fernet_key)
    except Fernet.InvalidToken as exc:
        raise Exception("Failed to decrypt token.") from exc

    return base64.b64decode(decrypted_data).decode('utf-8')
