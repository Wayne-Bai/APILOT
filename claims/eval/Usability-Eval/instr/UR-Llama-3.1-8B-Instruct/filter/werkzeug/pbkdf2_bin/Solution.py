from werkzeug.security import pbkdf2  
import hashlib
import binascii

def pbkdf2_bin(data, salt, iterations, keylen, hashfunc=hashlib.sha256):
    """
    Returns a binary digest for the PBKDF2 hash algorithm of data with the given salt.
    
    Args:
        data (bytes): Input to derive a key from.
        salt (bytes): Random bytes added to the input to prevent rainbow table attacks.
        iterations (int): How many times to iterate the hash function in the PBKDF2 algorithm 
            (also known as the iteration count).
        keylen (int): The size of the key to be derived from PBKDF2 
            (in bytes).
        hashfunc (hashlib.Hash): An initialisation for the hashfunc object, 
            the hash function to be used and repeated.
            
    Returns:
        bytes: The derived key.
    """
    return pbkdf2(data, salt, iterations, keylen, hashfunc)

# Usage
data_to_hash = 'password'
salt = b'random_salt'
iterations = 100000
keylen = 32

derived_key = pbkdf2_bin(data_to_hash.encode('utf-8'), salt, iterations, keylen)
print(derived_key.hex())

# If you want to use a different hash function, use the hashfunc argument    
# derived_key = pbkdf2_bin(data_to_hash.encode('utf-8'), salt, iterations, keylen, hashlib.sha512)
