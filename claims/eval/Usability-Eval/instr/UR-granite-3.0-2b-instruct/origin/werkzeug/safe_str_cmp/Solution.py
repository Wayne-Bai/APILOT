from werkzeug import secure_filename

def compare_strings(string1, string2, length):
    if len(string1) < length:
        string1 = string1.ljust(length)
    if len(string2) < length:
        string2 = string2.ljust(length)
    return (string1, string2)

# Example usage:
string1 = "hello"
string2 = "world"
length = 5

result = compare_strings(string1, string2, length)
print(result)  # Output: ('hello', 'world')
