import werkzeug.http

def parse_range_header(header):
    try:
        start, end = header.split("=")[1].split("-")
        start, end = int(start), int(end)
    except ValueError:
        return None
    return start, end

# Test the function
header = "bytes=100-200"
start, end = parse_range_header(header)
print(f"Start: {start}, End: {end}")
