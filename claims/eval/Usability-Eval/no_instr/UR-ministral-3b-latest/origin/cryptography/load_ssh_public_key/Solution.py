from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, utils

# του ASSUMING we have some SSH public key string data in "ssh_public_key"
ssh_public_key = "<your_ssh_public_key_string>"

# Programme logic
# First, convert the SSH public key string to a bytes object
ssh_public_key_bytes = ssh_public_key.encode('utf-8')

# Next, initialize a "PublicKey" base object and use this object to
# deserialize the byte object
pub_key = utils.DerivePrivatePublicKeyFactory(data=ssh_public_key_bytes)

# Finally, instantiate a "PublicKey" object using the derived private/public
# key pair parameters
public_key = utils.PublicKey(key_dictiontte, ssh_public_key)
