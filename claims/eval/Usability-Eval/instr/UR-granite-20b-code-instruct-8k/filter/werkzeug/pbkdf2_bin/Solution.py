
import hashlib

def pbkdf2_bin(data, salt, iterations=10000, keylen=24, hashfunc='sha256'):
    """Returns a binary digest for the PBKDF2 hash algorithm of data with the given salt."""
    if isinstance(data, str):
        data = data.encode('utf-8')
    if isinstance(salt, str):
        salt = salt.encode('utf-8')
    hasher = hashlib.new(hashfunc, b'' .join([salt, data]))
    def _pbkdf2(data, salt, iterations, keylen, hasher):
        """PBKDF2 key derivation function as defined by IEEE Std 802.11-2004."""
        d = b''
        for i in range(iterations):
            d = hasher(d + data + salt).digest()
        return d[:keylen]
    return _pbkdf2(data, salt, iterations, keylen, hasher)
