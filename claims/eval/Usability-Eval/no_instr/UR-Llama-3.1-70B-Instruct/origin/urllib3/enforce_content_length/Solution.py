import urllib.request
import warnings

# Suppress the ResourceWarning as we're handling a known case
warnings.simplefilter('ignore', ResourceWarning)

def enforce_content_length(url):
    """
    Enforce content length checking for the given URL.
    
    Args:
        url (str): The URL to check.

    Raises:
        ValueError: If the content length does not match the Content-Length header.
    """
    # Open the URL and get the info
    with urllib.request.urlopen(url) as response:
        # Get the Content-Length header if present
        content_length = response.headers.get('Content-Length')
        
        # If Content-Length header is present
        if content_length:
            # Convert to integer for comparison
            expected_length = int(content_length)
            
            # Read the content
            content = response.read()
            
            # Check if the lengths match
            if len(content)!= expected_length:
                raise ValueError(f"Content length mismatch. Expected {expected_length}, got {len(content)}")
        
        # If Content-Length header is not present, we cannot enforce the check
        else:
            print("Content-Length header not found. Cannot enforce content length check.")

# Test the function
enforce_content_length('http://example.com')
