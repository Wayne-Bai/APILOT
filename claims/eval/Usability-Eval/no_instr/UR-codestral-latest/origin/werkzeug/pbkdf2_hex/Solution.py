from werkzeug.security import pbkdf2_hex

def generate_password_hash(password, salt):
    # pbkdf2_hex returns a hex-encoded string
    hashed_password = pbkdf2_hex(password, salt, iterations=100000)
    return hashed_password

# Usage
password = "my_password"
salt = "my_salt"
hashed_password = generate_password_hash(password, salt)
print(hashed_password)
