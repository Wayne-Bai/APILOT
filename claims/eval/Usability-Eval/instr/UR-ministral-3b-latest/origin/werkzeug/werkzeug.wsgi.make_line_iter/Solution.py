from werkzeug.wrappers import Request, Response
import sys

def iterate_lines(stream):
    for line in stream.splitlines():
        yield line

# Simulating an input stream from a file-like object (e.g., a file)
class StreamReader:
    def __init__(self, filepath):
        self.stream = None
        self.filepath = filepath

    def line_callback(self, line):
        print(f"Processing line: {line}")

    def __iter__(self):
        self.stream = open(self.filepath, 'r')
        try:
            for line in iterate_lines(self.stream):
                self.line_callback(line)
        finally:
            self.stream.close()

# Example usage
if __name__ == '__main__':
    reader = StreamReader('example.txt')
    for line in reader:  # This should be called without __iter__
        print(line)
