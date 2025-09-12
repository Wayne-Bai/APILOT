from cryptography.fernet import Fernet

# Let's assume we have the key and token
key = b'your_secret_key'
token = b'your_fernet_token'

# Creating a Fernet object
cipher_suite = Fernet(key)

# Decrypt the token
try:
    plain_text = cipher_suite.decrypt(token)
    print("Decrypted text: ", plain_text.decode())
except Exception as e:
    print("An error occurred during decryption: ", str(e))
