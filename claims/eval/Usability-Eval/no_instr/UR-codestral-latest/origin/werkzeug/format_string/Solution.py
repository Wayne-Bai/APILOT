from werkzeug.utils import StringTemplate

template = StringTemplate("Hello, $name!")
formatted_string = template(name="John")
print(formatted_string)
