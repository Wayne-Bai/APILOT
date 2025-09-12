from typing import Callable, Tuple
import binascii
from werkzeug.security import pbkdf2
from typing import Optional

def pbkdf2_hex(
    password: bytes,
    salt: bytes,
    iterations: int,
    keysize: Optional[int] = None,
    hash_function: Callable = pbkdf2.prf_hmac("sha256"),
) -> Tuple[bytes, bytes]:
    """
    Similar to pbkdf2(), but returns a hexadecimal-encoded string.

    If you are only doing one PBKDF2 operation, it might be faster to just mix in.
    """
    key = pbkdf2(password, salt, iterations, keysize, hash_function, digestmod=hashlib.sha256)

    return binascii.hexlify(key).decode('ascii'), key

# Example usage:
password = b'mypassword'
salt = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x10\x11\x12\x13\x14\x15'
num_iterations = 10000
num_bytes = 32

digest, derived_key = pbkdf2_hex(password, salt, num_iterations, num_bytes)

print(f"Derived Key (hex): {digest}")
