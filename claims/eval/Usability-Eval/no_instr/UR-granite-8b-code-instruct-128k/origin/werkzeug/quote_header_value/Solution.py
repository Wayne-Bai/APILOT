from werkzeug.utils import quote_header_value
header_value = "Some Value"
quoted_value = quote_header_value(header_value)
print(quoted_value)
