from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import dates
from datetime import datetime, timedelta
import pytz

# Define the validity end date
valid_from_date = datetime(2023, 1, 1, tzinfo=pytz.UTC)
valid_to_date = valid_from_date + timedelta(days=365)

# Create a date representing the end of the validity period
validity_end_date = dates.HttpDate.validity_end(valid_to_date)

# Output the validity end date
print(validity_end_date)
