from datetime import datetime, timezone

# Get the current UTC time
now = datetime.now(timezone.utc)

# Format the time in RFC1123 format
formatted_time = now.strftime("%a, %d %b %Y %H:%M:%S GMT")

print(formatted_time)
