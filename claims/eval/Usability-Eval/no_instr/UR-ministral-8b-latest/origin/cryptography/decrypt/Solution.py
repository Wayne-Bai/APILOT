from cryptography.fernet import Fernet

def decrypt_fernet_token(token, key):
    try:
        # Initialize Fernet using the provided key
        fernet = Fernet(key)

        # Decrypt the token
        plaintext = fernet.decrypt(token)

        # Return the original plaintext
        return plaintext
    except Exception as e:
        # If there is an error during decryption, raise the exception
        raise e
