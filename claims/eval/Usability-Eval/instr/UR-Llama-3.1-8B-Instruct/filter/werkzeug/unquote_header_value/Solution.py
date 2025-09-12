from werkzeug.utils import unquote

def unquote_header(value):
    return unquote(value)

# Example usage
value = "Hello, World! how are you?"
unquoted_value = unquote_header(value)
print(unquoted_value)
