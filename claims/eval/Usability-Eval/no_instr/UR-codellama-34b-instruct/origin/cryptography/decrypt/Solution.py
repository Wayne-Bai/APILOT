
import fernet

# Define the key used to encrypt the data
key = b"your_secret_key_here"

# Define the nonce used to generate the token
nonce = b"your_nonce_here"

# Decrypt the Fernet token
token = b"your_fernet_token_here"
decrypted_data = fernet.Fernet(key, nonce).decrypt(token)

# If the decryption is successful, print the original plaintext data
if decrypted_data:
    print(f"Decrypted data: {decrypted_data}")
else:
    # If the decryption fails, an exception will be raised
    raise fernet.FernetError("Unable to decrypt the Fernet token.")
