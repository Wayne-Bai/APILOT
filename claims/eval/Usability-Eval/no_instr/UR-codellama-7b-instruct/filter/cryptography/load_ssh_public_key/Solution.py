
from cryptography.hazmat.primitives import serialization

# Deserialize a public key from OpenSSH (RFC 4253 and PROTOCOL.certkeys) encoded data to an instance of the public key type.
def deserialize_public_key(data):
    # Parse the public key data according to the RFC 4253 specification.
    parser = serialization.RFC4253Parser()
    parser.feed(data)
    # Build a PublicKey object from the parsed data.
    public_key = parser.public_key
    return public_key
