
import datetime
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Create a naïve datetime representing the beginning of the validity period for the certificate in UTC
validity_begin = datetime.datetime(2022, 1, 1, tzinfo=datetime.timezone.utc)

# Convert the naïve datetime to an ASN.1 GeneralizedTime object
generalized_time = x509.GeneralizedTime(validity_begin)

# Serialize the ASN.1 GeneralizedTime object to a byte string
serialized_time = generalized_time.dump()

# Parse the serialized ASN.1 GeneralizedTime object back into a naïve datetime
parsed_time = x509.GeneralizedTime.load(serialized_time)
