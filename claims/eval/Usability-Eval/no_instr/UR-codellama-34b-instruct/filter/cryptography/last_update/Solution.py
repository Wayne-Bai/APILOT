import cryptography
from datetime import datetime, timezone

current_time = datetime.now(tz=timezone.utc)
print("The current time is", current_time)
