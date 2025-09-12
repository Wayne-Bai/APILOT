
from datetime import datetime, timezone
import typing as t

# Generate a naïve datetime representing the end of the validity period for the certificate in UTC. This value is inclusive.
def generate_valid_end_date() -> datetime:
    # Set the date to be 10 years from now
    now = datetime.now(timezone.utc)
    valid_end_date = now + timedelta(days=365 * 10)

    return valid_end_date
