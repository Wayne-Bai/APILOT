# Import the necessary libraries
from cryptography.fernet import Fernet

def decrypt_fernet_token(encrypted_token):
    """
    Decrypts a Fernet token.

    Args:
        encrypted_token (str): The encrypted token to be decrypted.

    Returns:
        str: The decrypted plaintext.

    Raises:
        ValueError: If the encrypted token is invalid or corrupted.
    """

    # Generate a secret key (or use an existing one)
    # This secret key is used for both encryption and decryption
    secret_key = Fernet.generate_key()
    
    # Create a Fernet instance with the secret key
    fernet = Fernet(secret_key)

    # Try to decrypt the token
    try:
        # Decrypt the token using the Fernet instance
        decrypted_token = fernet.decrypt(encrypted_token.encode())

        # Decode the decrypted bytes to a string
        decrypted_text = decrypted_token.decode()

        # Return the decrypted text
        return decrypted_text

    except Exception as e:
        # If an error occurs during decryption, raise a ValueError
        raise ValueError("Failed to decrypt token: {}".format(str(e)))

# Example usage
encrypted_token = b'gddlnekuqgA____Ay6T_fzZ88MYb1Wanoj9fKtrDSV8='
try:
    decrypted_text = decrypt_fernet_token(encrypted_token)
    print("Decrypted Text: ", decrypted_text)
except ValueError as ve:
    print("Error: ", ve)
