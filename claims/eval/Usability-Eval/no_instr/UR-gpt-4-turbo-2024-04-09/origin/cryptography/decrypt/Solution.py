from cryptography.fernet import Fernet

def decrypt_fernet_token(key, token):
    """
    Decrypts a Fernet token using the provided key.

    Args:
        key (bytes): The secret key used to encrypt the token.
        token (bytes): The encrypted Fernet token.

    Returns:
        str: The decrypted plaintext if decryption is successful.

    Raises:
        cryptography.fernet.InvalidToken: If the token is invalid or has been tampered with.
    """
    fernet = Fernet(key)
    return fernet.decrypt(token).decode('utf-8')
