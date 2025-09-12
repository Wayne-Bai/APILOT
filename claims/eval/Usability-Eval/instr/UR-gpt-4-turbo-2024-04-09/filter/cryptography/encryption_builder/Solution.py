from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class EncryptionConfig:
    AES = 'aes'
    DES = 'des'
    
    def __init__(self, choice):
        self.choice = choice
        self.backend = default_backend()

    def configure_builder(self):
        if self.choice == self.AES:
            algorithm = algorithms.AES(self._generate_key())
            mode = modes.CBC(self._generate_iv())
            return Cipher(algorithm, mode, backend=self.backend)
        elif self.choice == self.DES:
            algorithm = algorithms.TripleDES(self._generate_key())
            mode = modes.CBC(self._generate_iv())
            return Cipher(algorithm, mode, backend=self.backend)
        else:
            raise ValueError("Unsupported encryption type selected")

    def _generate_key(self):
        # This is a placeholder function, in a real-world application
        # you must securely generate a suitable key
        return b'This is a key123'  # Example key

    def _generate_iv(self):
        # This is a placeholder function, in a real-world application
        # you must securely generate a suitable initial vector
        return b'This is an IV12'  # Example IV

# Example usage:
encryption_choice = EncryptionConfig(EncryptionConfig.AES)
cipher = encryption_choice.configure_builder()
encryptor = cipher.encryptor()

# `encryptor` can now be used to encrypt data
