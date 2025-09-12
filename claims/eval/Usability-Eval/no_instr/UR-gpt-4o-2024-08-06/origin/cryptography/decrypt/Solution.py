from cryptography.fernet import Fernet

# Suppose this is the key (in practice, securely generate and store this key)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Example encrypted token
encrypted_token = cipher_suite.encrypt(b"This is a secret message.")

# Decrypting the token
try:
    decrypted_text = cipher_suite.decrypt(encrypted_token)
    print("Decrypted text:", decrypted_text.decode('utf-8'))
except Exception as e:
    print("An error occurred during decryption:", str(e))
