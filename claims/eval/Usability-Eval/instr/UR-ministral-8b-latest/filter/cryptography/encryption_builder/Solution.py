from cryptography.fernet import Fernet

class EncryptionBuilder:
    def __init__(self):
        self.cipher = Fernet(generate_key())

    def configure_key(self):
        # Return the cipher key
        return self.cipher.key()

    def configure_salting(self):
        # Configure the salting strategy
        # For simplicity, we'll just return a fixed salt.
        return b'nonce'

    def configure_nonce(self):
        # Configure the nonce strategy
        # For simplicity, we'll return a fixed nonce.
        return b'nonce'

def generate_key():
    # Generate a new key
    return Fernet.generate_key()

# Usage example
builder = EncryptionBuilder()
print(builder.configure_key())
print(builder.configure_salting())
print(builder.configure_nonce())
