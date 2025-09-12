import os
from cryptography.fernet import Fernet

def get_encryption_builder():
    return Fernet()
