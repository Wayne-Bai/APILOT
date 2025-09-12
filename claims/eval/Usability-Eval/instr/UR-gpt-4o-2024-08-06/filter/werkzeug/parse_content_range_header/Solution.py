from werkzeug.http import parse_range_header

# Assuming you have a range header string, such as 'bytes=0-499'
range_header = 'bytes=0-499'

# Parse the range header
parsed_range = parse_range_header(range_header, make_content_range=True)

# Check and print the result
if parsed_range is not None:
    print("Parsed ContentRange:", parsed_range)
    print("Units:", parsed_range.units)
    print("Start:", parsed_range.start)
    print("Stop:", parsed_range.stop)
    print("Length:", parsed_range.length)
else:
    print("Parsing failed or resulted in None")
