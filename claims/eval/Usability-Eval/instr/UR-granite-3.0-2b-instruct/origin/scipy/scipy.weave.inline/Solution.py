# cython: language_level=3

def greet(string_list):
    for string in string_list:
        print("Hello, " + string)
