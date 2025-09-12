from werkzeug.security import generate_password_hash, check_password_hash
import binascii

def pbkdf2_hex(password, salt=None, iterations=100000, key_length=32):
    if salt is None:
        salt = generate_password_hash(password, method='sha256').salt

    password_hash = generate_password_hash(password, method='pbkdf2', iterations=iterations, key_length=key_length, salt=salt)
    return password_hash.hexdigest()
