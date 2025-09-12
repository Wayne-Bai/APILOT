from werkzeug.wrappers import Response

def string_template_format(name, age):
    # Using f-string for string formatting
    return f"Hello, {name}. You are {age} years old."

# Example usage
formatted_string = string_template_format("Alice", 30)
response = Response(formatted_string)
print(response.get_data(as_text=True))
