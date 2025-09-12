from cryptography.hazmat.primitives import serialization

def deserialize_public_key(openssh_data):
    # Decode the OpenSSH data from base64
    openssh_data = openssh_data.decode('base64')

    # Parse the OpenSSH data
    public_key_data = eval(openssh_data)

    # Deserialize the public key data
    public_key = serialization.load_pem_public_key(public_key_data)

    return public_key
