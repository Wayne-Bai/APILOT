from cryptography import x509
from datetime import datetime, timedelta

# Create a function to generate the naive datetime for the next CRL update
def generate_next_crl_update():
    # Current datetime
    now = datetime.now()
    # Example timedelta for next update (e.g., 30 days)
    next_update_period = timedelta(days=30)
    # Calculate next update datetime (naive, i.e., without timezone info)
    next_crl_update = now + next_update_period
    return next_crl_update

# Call the function to get the next CRL update time
next_crl_update = generate_next_crl_update()
print("Next CRL update is expected at:", next_crl_update)
