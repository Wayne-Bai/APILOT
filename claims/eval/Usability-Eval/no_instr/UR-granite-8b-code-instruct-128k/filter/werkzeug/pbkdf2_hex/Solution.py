from werkzeug.security import pbkdf2_bin
password = b"my_password"
salt = b"my_salt"
hash = pbkdf2_bin(password, salt, 100000)
hex_hash = hash.hex()
print(hex_hash)
