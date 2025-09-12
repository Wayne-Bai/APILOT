
from werkzeug.security import gen_salt

def pbkdf2_hex(password, salt):
    hash = gen_salt(password)
    return hash.encode("hex")

# Example usage:
print(pbkdf2_hex("mysecretpassword", "mysalt"))
