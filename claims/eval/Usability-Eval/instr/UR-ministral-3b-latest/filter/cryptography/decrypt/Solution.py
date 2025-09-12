from cryptography.fernet import Fernet
import base64

# Example key - this must be your actual Fernet key
fernet_key = Fernet.generate_key()
cipher_suite = Fernet(fernet_key)

def decrypt_data(encrypted_message):
    try:
        decrypted_message = cipher_suite.decrypt(encrypted_message)
        return decrypted_message.decode()
    except Exception as e:
        # Reraise the exception in case of decryption error
        raise Exception("Decryption failed: {}".format(str(e)))

# Example encrypted message (must be Base64 encoded in your use case)
encrypted_message = base64.b64decode(
    'gCCD8ff7aYed6bS6qj1EtQFT vast_vYG/jnFviBoTu74pUQ=')

# Decrypt the message
decrypted_plaintext = decrypt_data(encrypted_message)
print("Decryted Plaintext:", decrypted_plaintext)
