from datetime import datetime, timedelta
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key

# Generate a new private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Get the end of the validity period
end_date = private_key.public_key().valid_not_after()

# Convert the end date to UTC
end_date_utc = end_date.astimezone(datetime.utcfromtimestamp(0))

# Print the end date in UTC
print(end_date_utc)
