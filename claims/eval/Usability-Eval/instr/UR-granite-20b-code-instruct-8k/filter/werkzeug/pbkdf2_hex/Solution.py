import werkzeug

def generate_hex_encoded_string(password):
    """Generate a hex-encoded string using werkzeug.

    Args:
        password (str): The password to generate the hex-encoded string.

    Returns:
        str: The generated hex-encoded string.
    """
    hex_encoded_string = werkzeug.security.generate_password_hash(password)
    return hex_encoded_string
