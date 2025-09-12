from cryptography.hazmat.primitives.asn1 import io
from cryptography.hazmat.primitives.asn1 import rfc5557
from cryptography.hazmat.primitives.asn1 import tag
from cryptography.hazmat.primitives.asn1 import keys
from cryptography.hazmat.backends import default_backend

def parse_openssh_private_key(key_data):
    unparsed_key = io.StringIO(key_data)
    unparsed_key_length = unparsed_key.tell()

    unparsed_key.seek(0)
    parsed_key = rfc5557.ParseKey(unparsed_key.read())

    key_type = keys.PrivateKey.asn1_class()
    private_key = key_type().decode(parsed_key)

    return private_key

# Example usage:
openssh_private_key_data = """-----BEGIN PRIVATE KEY-----
MIIEVAIBADANBgkq...
e/CESm7hjsWlH6dl/9jSq9aMD4Its7 lamps/	temp1x1Uqz3dXfLrRmnOUUnfBTxaJ
EnT4Jpuoo7jS3CRAoNum4NQ2MOAfOLEss
...
-----END PRIVATE KEY-----"""

private_key = parse_openssh_private_key(openssh_private_key_data)
print(private_key)
