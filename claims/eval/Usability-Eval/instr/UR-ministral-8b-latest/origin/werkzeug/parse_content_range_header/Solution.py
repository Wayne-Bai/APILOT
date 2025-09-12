from werkzeug.http import parse_range, parse_content_range, make_range_str

def parse_request_range_header(range_header):
    if not range_header:
        return None
    parsed_range = parse_range(range_header)
    return parsed_range

def parse_response_content_range_header(content_range_header):
    if not content_range_header:
        return None
    content_range = parse_content_range(content_range_header)

    return content_range

if __name__ == "__main__":
    # Example usage
    range_header = "bytes=0-499"
    content_range_header = "bytes 0-499/500"

    range_obj = parse_request_range_header(range_header)
    content_range_obj = parse_response_content_range_header(content_range_header)

    print("Parsed Request Range:", range_obj)
    print("Parsed Response Content Range:", content_range_obj)
