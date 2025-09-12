
from werkzeug.security import safe_str_cmp

string1 = "Hello"
string2 = "World"

if len(string1) == len(string2):
    result = True
    for x, y in zip(string1, string2):
        if x != y:
            result = False
            break
else:
    result = False

print(result)
