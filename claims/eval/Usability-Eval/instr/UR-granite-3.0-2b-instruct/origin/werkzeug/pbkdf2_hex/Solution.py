from werkzeug.security import generate_password_hash, check_password_hash
import binascii

def pbkdf2_hex(password, salt=None, iterations=100000, hash_length=32):
    if salt is None:
        salt = generate_password_hash(password, method='sha256').hexdigest()
    else:
        salt = salt.encode('utf-8')
    password = password.encode('utf-8')
    hash_obj = hashlib.pbkdf2_hmac('sha256', salt, password, iterations, hash_length)
    return binascii.hexlify(hash_obj).decode('utf-8')
