from cryptography.hazmat.primitives.asymmetric import rsa

# Generate a new private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Get the corresponding public key
public_key = private_key.public_key()

# Print the public key
print(public_key.public_bytes(
    encoding=rsa.Encoding.OpenSSH,
    format=rsa.PublicKey.Format.OpenSSH
))
