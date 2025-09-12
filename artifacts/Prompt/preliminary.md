Please generate python code with {PACKAGE} to fulfill the purpose {DESCRIPTION}
NOTICE: You can't call any function from {BANNED_FUNCTIONS_LIST} for your any solutions.

Note that your response will be directly passed to generate Abstract Syntax Tree, SO NO OTHER WORDS except code solution in multi-line string format.
The solution should be """ """.

And I will provide you an example.

Input example:

Please generate python code with re to fulfill the purpose substituting occurrences of a pattern in a string with another string.
NOTICE: You can't call any function from [] for your any solutions.

Note that your response will be directly passed to generate Abstract Syntax Tree, SO NO OTHER WORDS except code solution in multi-line string format.
The format should be """ """.

Output Example:
"""
import re

def substitute_pattern(pattern, replacement, text):
    return re.sub(pattern, replacement, text)

pattern = r'\d+'  # Example pattern: replace digits
replacement = 'X'  # Example replacement: with 'X'
text = 'There are 123 apples and 456 oranges.'

result = substitute_pattern(pattern, replacement, text)
print(result)
"""


Your solution: """ """.
