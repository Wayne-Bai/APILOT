
# Import the Fernet class from the cryptography library
from cryptography.fernet import Fernet
import base64

# Generate a key for encryption and decryption
def generate_key():
    """Generates a Fernet key."""
    return Fernet.generate_key()

# Decrypt the Fernet token
def decrypt_token(token, key):
    """Decrypts a Fernet token.

    Args:
        token (str): The Fernet token to decrypt.
        key (str): The key used for decryption.

    Returns:
        str: The decrypted plaintext.

    Raises:
        Exception: If the decryption fails.
    """
    # Create a Fernet instance with the provided key
    fernet = Fernet(key)

    try:
        # Attempt to decrypt the token
        decrypted_token = fernet.decrypt(token)
        return decrypted_token.decode("utf-8")
    except Exception as e:
        # Raise an exception if the decryption fails
        raise Exception("Decryption failed: " + str(e))

# Usage example
if __name__ == "__main__":
    # Generate a new key
    key = generate_key()
    print("Generated Key: ", key)

    # Create a Fernet instance with the generated key
    fernet = Fernet(key)

    # Encrypt a message
    message = "Hello, World!"
    encrypted_token = fernet.encrypt(message.encode("utf-8"))
    print("Encrypted Message: ", encrypted_token)

    # Decrypt the token
    decrypted_message = decrypt_token(encrypted_token, key)
    print("Decrypted Message: ", decrypted_message)
