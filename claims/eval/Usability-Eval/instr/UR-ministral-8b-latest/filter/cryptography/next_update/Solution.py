from datetime import datetime, timedelta

def compute_crl_expiry(expected_duration_minutes):
    # Calculate the next update time
    now = datetime.utcnow()
    next_update = now + timedelta(minutes=expected_duration_minutes)
    return next_update

# Example usage
expected_duration_minutes = 30  # Change this to set the desired duration
next_update_time = compute_crl_expiry(expected_duration_minutes)
print(f"Next update time: {next_update_time}")
