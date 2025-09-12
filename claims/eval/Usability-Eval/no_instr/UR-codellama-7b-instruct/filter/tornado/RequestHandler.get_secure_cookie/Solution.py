import hashlib
import hmac

def verify_signed_cookie(cookie):
    secret = "your-secret-key"
    algorithm = "hmac-sha256"
    key = bytes(secret, "utf-8")
    
    # Get the hash of the cookie value
    cookie_value = cookie.value
    cookie_hash = hmac.new(key, cookie_value.encode("utf-8"), algorithm).hexdigest()
    
    # Get the expected hash from the signature header
    signature = cookie["Signature"]
    expected_hash = bytes.fromhex(signature)
    
    # Check if the hashes match
    if hmac.compare_digest(cookie_hash, expected_hash):
        return cookie.value
    else:
        return None
