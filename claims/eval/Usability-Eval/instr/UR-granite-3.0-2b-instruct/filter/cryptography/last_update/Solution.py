from cryptography import dateutil
from datetime import datetime

# Define the last update datetime
last_update = datetime(2022, 1, 1, 0, 0, 0)

# Convert the datetime to a cryptography dateutil datetime object
last_update_crypto = dateutil.datetime.fromisoformat(last_update.isoformat())

# Print the last update datetime
print("Last update datetime:", last_update_crypto)
