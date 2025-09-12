from werkzeug.datastructures import ImmutableMapping

# Sample string, can be replaced with any existing string
input_string = "Hello, {name}!"

# Define the substitutions as an ImmutableMapping object
substitutions = ImmutableMapping({'name': 'World'})

# Format the string
output_string = input_string.format_map(substitutions)

# Now, the output_string contains the formatted string: "Hello, World!"
print(output_string)
