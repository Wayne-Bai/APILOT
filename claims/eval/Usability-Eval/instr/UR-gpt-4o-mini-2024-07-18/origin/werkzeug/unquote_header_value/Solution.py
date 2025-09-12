from werkzeug.http import unquote

def unquote_header_value(header_value):
    return unquote(header_value)

# Example usage
if __name__ == "__main__":
    header_value = "some%20encoded%20value"
    unquoted_value = unquote_header_value(header_value)
    print(unquoted_value)  # Output: some encoded value
