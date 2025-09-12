from werkzeug.http import quote_header_value

def quote_header_if_needed(value):
    return quote_header_value(value)

header_value = "This is a spacey value"
quoted_value = quote_header_if_needed(header_value)
print(quoted_value)  # Outputs: This%20is%20a%20spacey%20value
