# Import the cryptography library with the Fernet module
from cryptography.fernet import Fernet, InvalidToken

def generate_key():
    """
    Generate a key for Fernet encryption/decryption.
    """
    key = Fernet.generate_key()
    return key

def encrypt_data(key, data):
    """
    Encrypt data using Fernet.
    :param key: Fernet key
    :param data: Data to encrypt
    :return: encrypted data
    """
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(key, encrypted_data):
    """
    Decrypt Fernet token.
    :param key: Fernet key
    :param encrypted_data: Encrypted data to decrypt
    :return: Decrypted data if successful
    """
    try:
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)
        return decrypted_data.decode()
    except InvalidToken:
        print("Invalid token. Possible data tampering detected.")
        return None

# Example usage
if __name__ == "__main__":
    key = generate_key()
    print("Generated Key: ", key)

    data = "Hello, World!"
    print("Original Data: ", data)

    encrypted_data = encrypt_data(key, data)
    print("Encrypted Data: ", encrypted_data)

    decrypted_data = decrypt_data(key, encrypted_data)
    print("Decrypted Data: ", decrypted_data)
