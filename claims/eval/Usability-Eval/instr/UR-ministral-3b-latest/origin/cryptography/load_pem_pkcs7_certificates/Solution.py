from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.multipart import Part
from cryptography.hazmat.primitives.pkcs7 import pkcs7
from cryptography.hazmat.primitives.padding import PKCS1Padding
from cryptography.hazmat.primitives.hash import SHA256
from cryptography.hazmat.primitives import hashes

# Dummy data that is assumed to be PEM encoded PKCS7 blob data
pkcs7_blob = ...  # Use your actual varible here

# Deserialize PKCS7 data
pkcs7_data = pkcs7_pkcs.Load_pkcs7_data(pkcs7_blob)

# Parse the data to find the certificates
certificate_blob = pkcs7_data.certificates[0:len(pkcs7_data.certificates)-1]

# The rest of the code to convert certificateBlob to list of Certificates goes here

