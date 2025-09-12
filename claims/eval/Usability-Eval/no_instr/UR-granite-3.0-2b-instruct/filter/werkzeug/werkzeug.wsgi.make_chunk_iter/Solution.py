from werkzeug.utils import secure_filename

def make_line_iter(file_path, separator="\n"):
    with open(file_path, "r") as file:
        lines = file.readlines()
    for line in lines:
        yield line.rstrip()

# Usage
for line in make_line_iter("example.txt", separator="\r\n"):
    print(line)
