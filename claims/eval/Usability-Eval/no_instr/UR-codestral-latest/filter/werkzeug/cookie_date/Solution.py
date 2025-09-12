from datetime import datetime

def format_rfc1123(dt):
    return dt.strftime("%a, %d %b %Y %H:%M:%S GMT")

# Example usage:
now = datetime.now()
formatted_now = format_rfc1123(now)
print(formatted_now)
