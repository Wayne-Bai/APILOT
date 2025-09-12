from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Create a Fernet cipher using the key
cipher = Fernet(key)

# Encrypt some data
data = b"Hello, world!"
cipher_text = cipher.encrypt(data)

# Decrypt the data
plain_text = cipher.decrypt(cipher_text)

# Print the decrypted data
print(plain_text.decode("utf-8"))
