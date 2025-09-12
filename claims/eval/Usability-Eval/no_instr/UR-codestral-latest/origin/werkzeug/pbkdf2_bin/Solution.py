import hashlib
import binascii

def generate_pbkdf2_digest(data, salt, iterations=100000, keylen=32, hash_name="sha256"):
    hash_func = getattr(hashlib, hash_name)
    dk = hashlib.pbkdf2_hmac(hash_func().name, data.encode(), salt, iterations, dklen=keylen)
    return binascii.hexlify(dk)
