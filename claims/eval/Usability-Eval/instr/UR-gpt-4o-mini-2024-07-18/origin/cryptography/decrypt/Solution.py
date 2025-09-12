from cryptography.fernet import Fernet

def decrypt_fernet_token(token: bytes, key: bytes) -> str:
    """
    Decrypts a Fernet token using the provided key.
    
    Args:
        token (bytes): The encrypted token to decrypt.
        key (bytes): The key used for decryption.
    
    Returns:
        str: The original plaintext if successfully decrypted.
    
    Raises:
        InvalidToken: If the token is invalid or the decryption fails.
    """
    fernet = Fernet(key)
    try:
        decrypted_data = fernet.decrypt(token)
        return decrypted_data.decode('utf-8')
    except Exception as e:
        raise Exception("Decryption failed") from e
