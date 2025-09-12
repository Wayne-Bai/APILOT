from werkzeug.security import pbkdf2_hex
import hashlib

def pbkdf2_hash(data, salt, iterations=100000, keylen=32, hashfunc=hashlib.sha256):
    # Convert the data to bytes if it's not already
    if not isinstance(data, bytes):
        data = data.encode('utf-8')
    
    # Convert the salt to bytes if it's not already
    if not isinstance(salt, bytes):
        salt = salt.encode('utf-8')
    
    # Generate the PBKDF2 hash in hexadecimal format
    hex_digest = pbkdf2_hex(data, salt, iterations, keylen, hashfunc)
    
    # Convert the hexadecimal digest to binary
    binary_digest = bytes.fromhex(hex_digest)
    
    return binary_digest
