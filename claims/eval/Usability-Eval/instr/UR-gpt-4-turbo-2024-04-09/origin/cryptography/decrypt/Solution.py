from cryptography.fernet import Fernet

def decrypt_token(key, token):
    try:
        fernet = Fernet(key)
        decrypted_message = fernet.decrypt(token)
        return decrypted_message
    except Exception as e:
        print("An error occurred:", e)
        raise

# Example usage:
key = Fernet.generate_key()  # Use this method to generate a new key, or use a pre-existing key
fernet = Fernet(key)
token = fernet.encrypt(b"Hello, world!")  # Encrypting a message first for demonstration

try:
    decrypted_message = decrypt_token(key, token)
    print("Decrypted message:", decrypted_message.decode())
except Exception as e:
    print("Failed to decrypt the message.")
