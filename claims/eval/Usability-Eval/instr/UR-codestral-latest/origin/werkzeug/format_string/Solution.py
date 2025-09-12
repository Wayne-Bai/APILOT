data = {
    'name': 'John Doe',
    'age': 30
}

formatted_string = "Hello, my name is {name} and I am {age} years old.".format(**data)
print(formatted_string)
