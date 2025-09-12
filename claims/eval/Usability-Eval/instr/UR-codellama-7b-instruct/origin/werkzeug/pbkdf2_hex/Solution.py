import hashlib
import binascii
def generate_password(password: str):
    salt = os.urandom(16)
    kdf = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return binascii.hexlify(kdf).decode()