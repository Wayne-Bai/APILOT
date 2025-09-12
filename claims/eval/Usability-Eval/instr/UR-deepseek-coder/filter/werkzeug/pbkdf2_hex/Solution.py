from werkzeug.security import pbkdf2_hex

def custom_pbkdf2_hex(password, salt, iterations, key_length):
    return pbkdf2_hex(password, salt, iterations, key_length)
