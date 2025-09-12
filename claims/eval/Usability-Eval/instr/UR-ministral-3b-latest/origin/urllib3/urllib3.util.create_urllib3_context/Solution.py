import urllib3

# Create a custom SSLContext instance
ctx = urllib3.util.ssl_.create_urllib3_context(
    secure=True,
    # other configuration parameters
)

# Example usage
print(f"SSLContext configuration: {ctx}")
