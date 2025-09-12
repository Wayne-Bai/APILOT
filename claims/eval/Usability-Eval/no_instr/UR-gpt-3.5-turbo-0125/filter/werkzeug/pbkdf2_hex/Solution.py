
from hashlib import pbkdf2_hmac
import binascii

def pbkdf2_hex(password, salt, iterations=100000, keylen=16, hashfunc='sha256'):
    dk = pbkdf2_hmac(hashfunc, password.encode(), salt, iterations, keylen)
    return binascii.hexlify(dk).decode()

# Example usage
password = "secretpassword"
salt = b'somesalt'
hex_encoded_password = pbkdf2_hex(password, salt)
print(hex_encoded_password)
