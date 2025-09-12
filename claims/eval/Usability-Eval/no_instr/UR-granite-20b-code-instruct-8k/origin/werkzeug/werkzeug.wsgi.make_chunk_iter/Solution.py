from werkzeug.utils import generate_password_hash

def make_chunk_iter(string, separator):
    chunks = string.split(separator)
    for chunk in chunks:
        yield chunk

string = "Hello World!"
separator = " "

for chunk in make_chunk_iter(string, separator):
    print(chunk)
