from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

# Generate a new DSA private key
private_key = dsa.generate(2048)

# Print the private key
print("Private Key:")
print(private_key.private_bytes(
    encoding=binascii.unhexlify,
    format=BinASCIIFormat.SSH2_PRIVATE_KEY,
    encryption_algorithm=NoEncryption()
))
