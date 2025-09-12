from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def generate_rsa_private_key():
    # Generate a new RSA private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key

def save_private_key_to_pem(private_key, file_path, password=None):
    # Serialize private key to PEM format
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(password) if password else serialization.NoEncryption()
    )
    
    # Save the PEM to a file
    with open(file_path, 'wb') as key_file:
        key_file.write(pem)
    
    print(f"Private key saved to {file_path}")

# Generate the RSA private key
private_key = generate_rsa_private_key()

# Save the private key to a file
save_private_key_to_pem(private_key, 'private_key.pem', password=b'mypassword')
