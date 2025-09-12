from cryptography.hazmat.primitives.asymmetric import dsa

# Generating parameters for DSA
key = dsa.generate_private_key(key_size=2048)

#here, key is our public key
public_key = key.public_key()

#private key related details
private_numbers = key.private_numbers()
print('private key parameters - ', private_numbers.parameter_numbers().x)

#public key related details
print('public key parameters - ', public_key.public_numbers().y)
