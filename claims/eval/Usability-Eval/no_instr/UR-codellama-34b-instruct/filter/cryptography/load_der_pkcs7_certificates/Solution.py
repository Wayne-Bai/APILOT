
import cryptography

# Load the DER-encoded PKCS7 data from a file
with open("pkcs7.der", "rb") as f:
    pkcs7_data = f.read()

# Create a new PKCS7 object from the data
pkcs7 = cryptography.hazmat.primitives.asymmetric.PKCS7(pkcs7_data)

# Extract the certificates from the PKCS7 object
certificates = pkcs7.get_certificates()

# Print the list of certificates
print("Certificates:")
for certificate in certificates:
    print(f"  {certificate.subject}")
