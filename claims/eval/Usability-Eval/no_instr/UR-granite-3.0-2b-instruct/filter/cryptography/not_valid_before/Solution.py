from cryptography import datetime

# Create a naïve datetime representing the beginning of the validity period for the certificate in UTC
validity_period_start = datetime.datetime.now(datetime.UTC)
