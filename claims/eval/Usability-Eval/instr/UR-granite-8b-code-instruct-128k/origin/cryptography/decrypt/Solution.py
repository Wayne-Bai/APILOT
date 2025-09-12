
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Create a Fernet cipher
cipher = Fernet(key)

# Encrypt a message
message = b"Hello, world!"
cipher_text = cipher.encrypt(message)
print("Encrypted message:", cipher_text)

# Decrypt the message
plain_text = cipher.decrypt(cipher_text)
print("Decrypted message:", plain_text.decode())
