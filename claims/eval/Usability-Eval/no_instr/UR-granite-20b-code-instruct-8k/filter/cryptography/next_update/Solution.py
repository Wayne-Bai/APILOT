
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Load the certificate
with open("my_cert.pem", "rb") as f:
    cert = x509.load_pem_x509_certificate(f.read(), default_backend())

# Get the notAfter value from the certificate's extensions
not_after = cert.extensions.get_extension_for_class(
    x509.SubjectAlternativeName
).value

# Print the notAfter value
print(not_after)
