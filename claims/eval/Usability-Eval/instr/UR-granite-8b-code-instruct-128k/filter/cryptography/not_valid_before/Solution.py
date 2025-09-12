from cryptography import datetime

# Naive datetime representing the beginning of the validity period for the certificate in UTC. This value is inclusive.
validity_start = datetime.datetime(2022, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
