from cryptography.fernet import Fernet, InvalidToken

def decrypt_fernet_token(token: bytes, key: bytes) -> bytes:
    try:
        fernet = Fernet(key)
        plaintext = fernet.decrypt(token)
        return plaintext
    except InvalidToken:
        raise ValueError("Decryption failed or the token is invalid.")

# Example usage:
# key = Fernet.generate_key()  # This should be the key used to encrypt the data
# token = fernet.encrypt(b"Secret message")

# Assuming 'token' and 'key' are defined
# try:
#     decrypted_data = decrypt_fernet_token(token, key)
#     print("Decrypted text:", decrypted_data.decode())
# except ValueError as e:
#     print(e)
