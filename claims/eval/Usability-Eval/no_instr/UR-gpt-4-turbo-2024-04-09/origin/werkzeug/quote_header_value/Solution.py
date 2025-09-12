from werkzeug.http import quote_header_value

# Example usage:
header_value = "This is a test header with space and commas, perhaps?"
quoted_value = quote_header_value(header_value)
print("Quoted Header Value:", quoted_value)
