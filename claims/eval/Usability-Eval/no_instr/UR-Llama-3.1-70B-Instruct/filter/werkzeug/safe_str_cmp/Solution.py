import time
import hmac
from werkzeug.utils import secure_filename
from werkzeug.exceptions import BadRequest

def secure_compare(a, b):
    return hmac.compare_digest(a, b)

def constant_time_compare(val1, val2):
    if len(val1)!= len(val2):
        return False
    return hmac.compare_digest(val1, val2)

# Example usage
test_string1 = "Hello, World!"
test_string2 = "Hello, World!"

start_time = time.time()
result = secure_compare(test_string1, test_string2)
end_time = time.time()

print(f"Time taken for secure compare: {end_time - start_time} seconds")

start_time = time.time()
result = constant_time_compare(test_string1, test_string2)
end_time = time.time()

print(f"Time taken for constant time compare: {end_time - start_time} seconds")

test_string1 = "Hello, World!"
test_string2 = "Hello, World!1"

start_time = time.time()
result = secure_compare(test_string1, test_string2)
end_time = time.time()

print(f"Time taken for secure compare (strings don't match): {end_time - start_time} seconds")

start_time = time.time()
result = constant_time_compare(test_string1, test_string2)
end_time = time.time()

print(f"Time taken for constant time compare (strings don't match): {end_time - start_time} seconds")

try:
    constant_time_compare(test_string1, test_string2)
except BadRequest as e:
    print(e)

try:
    secure_filename("example.txt")
    print("File name is secure")
except BadRequest as e:
    print(e)
