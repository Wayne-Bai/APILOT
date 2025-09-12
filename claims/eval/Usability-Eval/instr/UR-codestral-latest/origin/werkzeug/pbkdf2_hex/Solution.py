from werkzeug.security import pbkdf2_bin
import base64

def pbkdf2_hex(password, salt, iterations, keylen):
    bin_hash = pbkdf2_bin(password, salt, iterations, keylen)
    hex_hash = base64.b16encode(bin_hash).decode('utf-8')
    return hex_hash
