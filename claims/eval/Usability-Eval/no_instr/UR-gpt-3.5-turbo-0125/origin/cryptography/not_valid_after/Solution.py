
from datetime import datetime, timedelta

# Generate a naïve datetime representing the end of the validity period for the certificate in UTC
validity_period_days = 30  # Example validity period of 30 days
end_validity_datetime = datetime.utcnow() + timedelta(days=validity_period_days)

print("End of validity period for the certificate (inclusive) in UTC:", end_validity_datetime)
