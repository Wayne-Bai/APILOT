from typing import Iterable

def make_line_iter(string: str, max_chunk_length: int = 79, 
                   separator: str ='', 
                   chunk_prefix: str = '') -> Iterable[str]:
    """
    This function generates an iterator that breaks a string into lines of 
    reasonable length and returns them one by one. It takes into account 
    the max_chunk_length, separator, and chunk_prefix.

    Args:
        string (str): The input string to be segmented.
        max_chunk_length (int): The maximum length of a chunk (default is 79).
        separator (str): The separator which divides chunks (default is'').
        chunk_prefix (str): The prefix of each chunk (default is '').

    Yields:
        str: Each line in the string.
    """

    word = ''
    line = ''

    for char in string:

        if char == separator:
            if len(line) + len(word) + 1 <= max_chunk_length:
                line = line + word + char
            else:
                yield chunk_prefix + line
                line = chunk_prefix + char
                word = ''
        elif char == '\n':
            if line:
                yield chunk_prefix + line
            yield chunk_prefix + char
            line = ''
        else:
            if len(word) + len(char) + (1 if line else 0) <= max_chunk_length:
                if line:
                    line = line + char
                else:
                    line = char
                word = ''
            else:
                if line:
                    yield chunk_prefix + line
                    line = ''
                yield chunk_prefix + word + char
                word = ''

    if line:
        yield chunk_prefix + line
    if word:
        yield chunk_prefix + word

    if string and string[-1]!= '\n':
        yield '\n'

# Example usage
string = "This is a really long string that needs to be segmented into multiple lines, each of a reasonable length."
max_chunk_length = 20
separator =''
chunk_prefix = '> '

for chunk in make_line_iter(string, max_chunk_length, separator, chunk_prefix):
    print(chunk)
