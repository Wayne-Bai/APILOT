from werkzeug.security import pbkdf2_hash

# Define the data to be hashed
data = b"password123"

# Define the salt (random value added to the data to prevent rainbow table attacks)
salt = b"thisisarandomsaltvalue"

# Define the number of iterations (higher values increase computational time and resistance to brute-force attacks)
iterations = 100000

# Define the key length in bytes (the output will be a binary digest of this length)
keylen = 32

# Use pbkdf2_hash from Werkzeug to generate the hash
digest = pbkdf2_hash(data, salt, iterations, keylen=keylen)

print("Binary digest:", digest)
