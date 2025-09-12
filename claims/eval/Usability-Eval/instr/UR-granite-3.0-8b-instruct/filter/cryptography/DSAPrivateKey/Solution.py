from cryptography.hazmat.primitives.asymmetric import dsa

# Generate a new private key
private_key = dsa.DSAPrivateKey.generate(2048)

# Print the private key
print(private_key.private_numbers())
