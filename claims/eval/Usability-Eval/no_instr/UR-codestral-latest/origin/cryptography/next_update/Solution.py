import datetime
import cryptography

# Assuming you have the next update information
# The example below assumes the information is in seconds from now
seconds_to_next_update = 3600  # For example, in 1 hour

# Get the current datetime
now = datetime.datetime.now()

# Compute the datetime for the next update
next_update = now + datetime.timedelta(seconds=seconds_to_next_update)

print(f'The next update to this CRL is expected at: {next_update}')
