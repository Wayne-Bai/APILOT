
from werkzeug.security import pbkdf2_bin
from binascii import b2a_hex

password = "test"
salt = os.urandom(8)
iterations = 1000
hash_len = 32

pbkdf2_hashed_password = pbkdf2_bin(password, salt, iterations, hash_len)
hex_encoded_password = b2a_hex(pbkdf2_hashed_password).decode("utf-8")
print(hex_encoded_password)
