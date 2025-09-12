from cryptography.fernet import Fernet

# Example usage
def decrypt_fernet_token(encrypted_data, key):
    try:
        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data)
        return decrypted_data.decode()
    except Exception as e:
        print(f"Failed to decrypt: {e}")
        return None

# Sample encrypted data and key (for testing purposes, use secure key in real applications)
encrypted_data = b'gAAAAABdqU7aKjj[- paralleT178aoG-kWZbps2rSNzgwS8umDaw=='
key = b'yourquixtyfourbytekeyLmeenteredquiingly='

# Call the function to decrypt the Fernet token
print(decrypt_fernet_token(encrypted_data, key))
