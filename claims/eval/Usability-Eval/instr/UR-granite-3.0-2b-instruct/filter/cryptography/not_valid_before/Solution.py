from cryptography import DateTime

# Define the start date and time for the validity period
start_datetime = DateTime.UtcNow.replace(hour=0, minute=0, second=0, microsecond=0)

# Set the end date and time for the validity period
end_datetime = start_datetime + timedelta(days=365)

# Create a datetime object representing the beginning of the validity period
start_validity_datetime = DateTime.from_datetime(start_datetime)

# Set the end date and time for the validity period
end_validity_datetime = DateTime.from_datetime(end_datetime)

# Print the start and end validity dates and times
print("Start validity date and time:", start_validity_datetime)
print("End validity date and time:", end_validity_datetime)
