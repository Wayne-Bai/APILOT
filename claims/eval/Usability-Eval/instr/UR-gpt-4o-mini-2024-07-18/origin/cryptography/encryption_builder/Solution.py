from cryptography.fernet import Fernet

class EncryptorBuilder:
    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(key)

    def encrypt(self, data):
        """Encrypts the given data."""
        if isinstance(data, bytes):
            return self.fernet.encrypt(data)
        elif isinstance(data, str):
            return self.fernet.encrypt(data.encode())
        else:
            raise ValueError("Data must be bytes or str.")

    def decrypt(self, token):
        """Decrypts the given token."""
        return self.fernet.decrypt(token).decode()

# Example usage:
if __name__ == "__main__":
    key = Fernet.generate_key()
    builder = EncryptorBuilder(key)

    original_data = "Hello, World!"
    encrypted_data = builder.encrypt(original_data)
    print("Encrypted:", encrypted_data)

    decrypted_data = builder.decrypt(encrypted_data)
    print("Decrypted:", decrypted_data)
