from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend
# Generate a DSA key pair
key_pair = dsa.generate_private_key(
    key_size=1024,
    generator=2,
    backend=default_backend()
)
# Get the public key from the private key
public_key = key_pair.public_key()
# Get the public key parameters
public_numbers = public_key.public_numbers()
# Print the public key parameters
print("Public Key Parameters:")
print("Y:", public_numbers.y)
print("G:", public_numbers.g)
print("P:", public_numbers.p)
print("Q:", public_numbers.q)
