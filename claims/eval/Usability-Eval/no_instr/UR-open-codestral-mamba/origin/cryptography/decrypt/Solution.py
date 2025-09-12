from cryptography.fernet import Fernet

def decrypt_token(token, key):
    cipher_suite = Fernet(key)
    try:
        decrypted_data = cipher_suite.decrypt(token)
        return decrypted_data.decode()
    except Exception as e:
        raise e

# Example usage:

# Make sure to generate your own key and token safely, for demonstration purposes, I'm using a placeholder

key = b'tAmkj45yorMdDb3IY0TNfLLao9fdKxkH3u059H0jexs='
token = b'gAAAAABd2LoY_EFpzJwAIzJ5uFkq5kPlHDdnwAFDM8CMnq4c5zEal5QEukpvF6RQnMGByzkehEd5D6RQ6ND7YXoQ=='

try:
    decrypted_text = decrypt_token(token, key)
    print(f"Decrypted message: {decrypted_text}")
except Exception as e:
    print(f"Error occurred while decrypting:{e}")
