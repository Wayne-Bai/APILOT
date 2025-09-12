from werkzeug.http import parse_content_range

# Example usage:
header = "range: bytes=0-4095"
content_range = parse_content_range(header)
if content_range:
    print("ContentRange: ", content_range)
else:
    print("Failed to parse ContentRange")
