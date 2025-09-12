from cryptography.fernet import Fernet

# This is a safe key to use for demonstration purposes. Make sure to use a secure key in a production environment.
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def decrypt_fernet_token(cipher_text):
    try:
        plain_text = cipher_suite.decrypt(cipher_text)
        return plain_text.decode()
    except Exception as e:
        raise Exception(f"Failed to decrypt token: {e}")

# Example usage
cipher_text = cipher_suite.encrypt(b'This is a secret message.')
print(decrypt_fernet_token(cipher_text))
