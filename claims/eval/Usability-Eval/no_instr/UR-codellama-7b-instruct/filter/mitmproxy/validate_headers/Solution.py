
from mitmproxy import http

def validate_headers(headers):
    """Validates that the given HTTP headers are not malformed.
    
    Args:
        headers (dict): The HTTP headers to be validated.
    
    Raises:
        ValueError: If the headers are malformed.
    """
    # Validate that all headers have a name and value
    if any(not isinstance(header, tuple) for header in headers):
        raise ValueError("Malformed HTTP headers")
    
    # Validate that no headers have an illegal character
    illegal_characters = ["\r", "\n"]
    if any(illegal_character in header[0] or header[1] for header in headers for illegal_character in illegal_characters):
        raise ValueError("Illegal characters in HTTP headers")
    
    # Validate that no headers have a name or value that is too long
    if any(len(header[0]) > 64 or len(header[1]) > 256 for header in headers):
        raise ValueError("HTTP header names and values must be less than 64 characters long")
    
    # Validate that no headers have a name or value that is too short
    if any(len(header[0]) < 1 or len(header[1]) < 1 for header in headers):
        raise ValueError("HTTP header names and values must be at least 1 character long")
