from werkzeug.security import generate_password_hash

password = "$2b$12$4624mydxwdflmRxa6KqDPuGzFjngPCfB"  # Example hash output
password_hash = generate_password_hash(password, method='pbkdf2', salt_length=16)
print(password_hash)
