from werkzeug.http import unquote_header

def unquote_value(header_value):
    return unquote_header(header_value)

# Example usage
header_value = "%41%6D%65%72%69%63%61%20%46%6F%6F%62%61%72"
print(unquote_value(header_value)) # Output: "America Foobar"
