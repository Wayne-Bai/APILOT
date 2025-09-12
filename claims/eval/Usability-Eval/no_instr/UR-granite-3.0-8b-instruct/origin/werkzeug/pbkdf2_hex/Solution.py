from werkzeug.security import generate_password_hash

def generate_hex_hash(password):
    return generate_password_hash(password, method='sha256').decode('utf-8')
