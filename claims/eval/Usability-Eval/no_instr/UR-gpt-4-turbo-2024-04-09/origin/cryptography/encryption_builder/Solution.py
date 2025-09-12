from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

class EncryptorBuilder:
    def __init__(self, public_key):
        self.public_key = public_key
        self._padding = padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
        self._encoding = Encoding.DER

    def with_padding(self, padding_scheme):
        self._padding = padding_scheme
        return self

    def with_encoding(self, encoding_type):
        self._encoding = encoding_type
        return self

    def encrypt(self, message):
        message_bytes = message.encode('utf-8')
        encrypted = self.public_key.encrypt(
            message_bytes,
            self._padding
        )
        return encrypted

# Example usage:

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import PublicFormat

# Generate or load a public key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Configure builder
builder = EncryptorBuilder(public_key)
builder.with_padding(padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA1()),
    algorithm=hashes.SHA1(),
    label=None
))
builder.with_encoding(Encoding.PEM)

# Encrypt a message
encrypted_message = builder.encrypt('Hello, World!')
print(encrypted_message)
