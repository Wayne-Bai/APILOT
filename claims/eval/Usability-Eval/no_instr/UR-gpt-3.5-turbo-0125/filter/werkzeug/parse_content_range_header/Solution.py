
from werkzeug.http import parse_content_range

header = "bytes 0-499/10000"
content_range = parse_content_range(header)

if content_range:
    print("Start: ", content_range.start)
    print("Stop: ", content_range.stop)
    print("Total Length: ", content_range.length)
else:
    print("Could not parse the range header.")
