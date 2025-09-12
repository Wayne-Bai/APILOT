import hashlib
import binascii
import hmac

def pbkdf2_hex(data, salt, iterations=10000, keylen=None, hashfunc=hashlib.sha256):
    """
    Returns a binary digest for the PBKDF2 hash algorithm of data with the given salt.
    It iterates iterations times and produces a key of keylen bytes.
    By default, SHA-256 is used as hash function; a different hashlib hashfunc can be provided.

    :param data: The byte string to be hashed.
    :param salt: The salt value used to produce the key.
    :param iterations: The number of iterations to perform the hash function.
    :param keylen: The length of the key. Default is 32 bytes.
    :param hashfunc: The hash function to use. Default is SHA-256 (hashlib.sha256).
    :return: A string representation of the binary digest, in hexadecimal form.
    """
    # Initialize the hash object
    hash_object = hashfunc()
    
    # Perform the hash function iterations
    for i in range(iterations):
        # Update the hash object with the salt and the data
        hash_object.update(salt + data + i.to_bytes(4, 'big'))

    # Get the extracted digest, truncated to the key length
    raw_key = hash_object.digest()

    # Truncate the digest to the key length
    key = raw_key[:keylen]

    # Convert the binary digest to hexadecimal
    return binascii.hexlify(key).decode()

# Test the function
data = b"password"
salt = b"random_salt_value"
print(pbkdf2_hex(data, salt))
