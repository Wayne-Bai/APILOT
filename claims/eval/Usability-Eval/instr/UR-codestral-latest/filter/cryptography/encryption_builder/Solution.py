from cryptography.fernet import Fernet

def get_configured_fernet_builder():
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    return cipher_suite

# Usage
cipher_suite = get_configured_fernet_builder()
text = "my secret message".encode()
cipher_text = cipher_suite.encrypt(text)
