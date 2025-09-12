from cryptography import x509
from datetime import datetime, timedelta

# Naïve datetime representing the end of the validity period for the certificate
validity_period_days = 365  # Example validity period of 1 year
end_validity_date = datetime.utcnow() + timedelta(days=validity_period_days)

# The value is inclusive
print("End of validity period (UTC):", end_validity_date)
