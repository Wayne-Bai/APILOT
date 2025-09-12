from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

def deserialize_openssh_public_key(public_key_data):
    # Remove the 'ssh-rsa' prefix and the newline character
    public_key_data = public_key_data.replace('ssh-rsa', '').strip()

    # Decode the base64 encoded data
    public_key_data = public_key_data.encode()

    # Load the public key from the data
    public_key = ec.ELDiffieHellman.load_ssh_public_key_from_data(public_key_data)

    return public_key
