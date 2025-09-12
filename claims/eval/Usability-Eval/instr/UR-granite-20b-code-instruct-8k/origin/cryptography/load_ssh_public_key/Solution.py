from cryptography.hazmat.primitives import serialization

def load_ssh_public_key(data):
    try:
        # Check if the data is in RFC 4253 format
        public_key = serialization.load_ssh_public_key(data)
    except ValueError:
        # If not, try PROTOCOL.certkeys format
        public_key = serialization.load_ssh_public_key_protocol_certkeys(data)

    return public_key
