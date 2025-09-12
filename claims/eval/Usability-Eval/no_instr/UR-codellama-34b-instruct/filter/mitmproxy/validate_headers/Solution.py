import mitmproxy

def validate_headers(headers):
    # Check for multiple headers with the same name
    for header_name in headers.keys():
        if len(headers[header_name]) > 1:
            raise ValueError("Multiple headers with the same name are not allowed")

    # Check for invalid characters in header names and values
    for header_name, header_value in headers.items():
        if any(c not in string.ascii_letters + string.digits + "_-." for c in header_name):
            raise ValueError("Invalid character in header name")
        if any(c not in string.printable for c in header_value):
            raise ValueError("Invalid character in header value")

# Example usage
headers = {"Host": "example.com", "User-Agent": "Mozilla/5.0"}
validate_headers(headers)  # No error is raised

headers = {"Host": "example.com", "User-Agent": "Mozilla/5.0\nInvalid character in header value"}
try:
    validate_headers(headers)
except ValueError as e:
    print("Validation failed: {}".format(e))  # Outputs "Validation failed: Invalid character in header value"
