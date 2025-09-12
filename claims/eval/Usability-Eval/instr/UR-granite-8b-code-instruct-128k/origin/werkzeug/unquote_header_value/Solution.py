from werkzeug.http import unquote

header_value = "Hello, World!"
unquoted_value = unquote(header_value)

print(unquoted_value)  # Output: "Hello, World!"
