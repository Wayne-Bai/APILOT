
from datetime import datetime, timedelta

validity_period = 30  # Validity period in days
start_date = datetime.utcnow()
end_date = start_date + timedelta(days=validity_period)
end_date_utc = end_date.replace(tzinfo=None)

print(f"End of validity period (UTC): {end_date_utc}")
