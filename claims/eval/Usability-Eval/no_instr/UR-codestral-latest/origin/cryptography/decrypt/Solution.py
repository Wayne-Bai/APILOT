from cryptography.fernet import Fernet

# Assuming you have the secret key
key = b'your_secret_key_here'

# Create a Fernet object with the key
cipher_suite = Fernet(key)

# Let's assume you have the encrypted token
token = b'your_encrypted_token_here'

try:
    # Decrypt the token
    plaintext = cipher_suite.decrypt(token)
    print(plaintext.decode())  # Decoded from bytes to string
except cryptography.fernet.InvalidToken:
    print("Invalid token. The token has been tampered with or is corrupted.")
