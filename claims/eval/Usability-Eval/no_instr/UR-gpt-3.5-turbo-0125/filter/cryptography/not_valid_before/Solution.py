
from datetime import datetime

# Define a function to calculate the start of the validity period for the certificate in UTC
def calculate_validity_start():
    # Retrieve the current UTC datetime
    current_utc_datetime = datetime.utcnow()

    return current_utc_datetime

# Call the function to get the start of the validity period
validity_start = calculate_validity_start()

print(f"The start of the validity period for the certificate in UTC is: {validity_start}")
