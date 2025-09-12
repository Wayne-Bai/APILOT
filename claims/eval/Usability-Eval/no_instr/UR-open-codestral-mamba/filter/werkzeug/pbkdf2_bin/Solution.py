from werkzeug.security import generate_password_hash, check_password_hash

# To generate PBKDF2 hash
password = "my_password"
salt = "my_salt"
hash_value = generate_password_hash(password, salt)
print("PBDKF2 hash: ", hash_value)

# To verify the hash
check_hash = check_password_hash(hash_value, password)
print("Hash verification: ", check_hash)
