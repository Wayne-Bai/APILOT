
from cryptography.fernet import Fernet

# Key for decrypting
key = b'your_key_here'

# Fernet token to decrypt
token = b'your_token_here'

# Initialize the Fernet object with the key
cipher = Fernet(key)

try:
    # Decrypt the token
    plaintext = cipher.decrypt(token).decode()
    print("Decrypted Plaintext:", plaintext)
except Exception as e:
    print("Decryption failed:", e)
