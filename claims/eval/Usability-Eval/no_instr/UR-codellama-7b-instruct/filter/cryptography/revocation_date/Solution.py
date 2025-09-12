import hashlib
def format_date(today):
    return today
# get the current date
today = datetime.date.today()
now = today.replace(tzinfo=timezone.utc)
revoked = format_date(now)
print(revoked)

