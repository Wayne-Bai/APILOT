from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()

# Create an encryption object using the key
cipher_suite = Fernet(key)

# Define the value to be encrypted
value = "your-secret-value"

# Encrypt the value
encrypted_value = cipher_suite.encrypt(value.encode())

print(f"Encrypted Value: {encrypted_value}")
