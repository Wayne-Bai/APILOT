from werkzeug.security import generate_password_hash, check_password_hash
import hashlib

def pbkdf2_hash(data: str, salt: str, iterations: int = 100000, keylen: int = 32, hashfunc: callable = hashlib.sha256) -> bytes:
    return hashlib.pbkdf2_hmac(hashfunc().name, data.encode(), salt.encode(), iterations, dklen=keylen)

# Example usage
data = "password"
salt = "random_salt"
hashed = pbkdf2_hash(data, salt)
print(hashed)
