from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives.serialization import load_ssh_public_key
from cryptography.hazmat.backends import default_backend

def deserialize_public_key(ssh_public_key):
    # Load the SSH public key from the string
    s = load_ssh_public_key(bytes(ssh_public_key, 'utf-8'), default_backend())

    # Return the public key instance
    return s

# A sample OpenSSH encoded key
openssh_public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCXyPhQs5Y4bJ0dZvMgzveSkLdAIFQDDOLiLJ0ID2YBxX0hpLWCRWYpyqShQbNxuD07QYsrnYXC3ErOCSOOkp+9+USuEwhH4i28QzNtyg81/LUIrUQt2K8WHN2ta/RTEF/yCu88mkoDnSm2LaECXHdRDPY0RS2QE9P/E1kC7psWdNH5eWcr5qpWszrR59vTlU+BJaiNgNdFNHJmRCeUHsZb6EgJCOOvVkc2s8v9l3Bv1kcXw0+Uz/OT3DaZ4bD0CVQlr3n/tSW89lN8X0hrGdb/ovYE8XBXdO1dV67RDT+OFM9lGztVVffo91DsrTI8QK10HH9JW5mhgZS7NSOn45CLz3vPS4G5am stereo@adam.sville"

public_key = deserialize_public_key(openssh_public_key)

print(public_key)
