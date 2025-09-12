from werkzeug.security import pbkdf2_bin, check_password_hash
import binascii

def pbkdf2_hex(password, salt, iterations, keylen):
    """
    Generates an PBKDF2 using the given password, salt, iterations and key length.
    
    :param password: The password to derive the key from
    :param salt: The salt to use
    :param iterations: The number of iterations
    :param keylen: The length of the key in bytes
    :return: A hex-encoded string of the derived key
    """
    raw_hash = pbkdf2_bin(password, salt, iterations, keylen).hex()
    return raw_hash

# Example usage:
password = b'supercalifragilisticexpialidocious'
salt = b'\x96\x15\xb5'
iterations = 1000
keylen = 32

print(pbkdf2_hex(password, salt, iterations, keylen))
