from werkzeug.security import generate_password_hash

# Function to generate PBKDF2 HMAC-SHA1 hash with a random salt followed by encoding the result to hex

def pbkdf2_bin_to_hex(password, salt, iterations=1000, key_length=20, hashing_method='sha1'):
    hash_value = generate_password_hash(password, method='pbkdf2:{}{}{}'.format(hashing_method, salt, iterations), salt_length=len(salt), key_length=key_length)
    return hash_value

# Let's test this function

password = 'mypassword'
salt = 'mysalt'
hex_string = pbkdf2_bin_to_hex(password, salt)
print(hex_string)
