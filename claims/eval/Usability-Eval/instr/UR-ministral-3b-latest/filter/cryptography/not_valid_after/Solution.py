import datetime
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography import x509

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Log a typical A certificate name and not_valid_after datetime
validity = datetime.timedelta(days=90)

# Calculate the occurring datetime of the end of certificate validity period in UTC
end_of_validity = datetime.datetime.utcnow() + validity

# Action here
## Output the end_of_validity datetime
