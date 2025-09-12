from cryptography.hazmat.primitives.asymmetric import dsa

# Generate a new DSA private key
private_key = dsa.generate_private_key(
    algorithm=dsa.DSA(hashes.SHA256()),
    key_size=2048
)

# Print the private key
print(private_key.private_bytes(
    encoding=Encoding.PEM,
    format=PrivateFormat.PKCS8,
    encryption_algorithm=EncryptionAlgorithm.AES256(private_key)
))
