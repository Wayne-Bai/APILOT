
import cryptography
from datetime import datetime, timedelta

# Create a naïve datetime representing the end of the validity period for the certificate in UTC
end_date = datetime(2023, 1, 1)

# Convert the datetime to a string in the format YYYY-MM-DDTHH:mm:ssZ (ISO 8601 with milliseconds and timezone offset)
end_date_string = end_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
