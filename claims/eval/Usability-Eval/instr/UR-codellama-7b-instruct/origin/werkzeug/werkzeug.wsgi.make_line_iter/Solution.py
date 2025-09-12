from werkzeug.stream import IterInputStream

def safe_readlines(stream):
    """Safely reads lines from a given input stream."""
    for chunk in stream:
        yield from chunk.split(b'\n')

# Example usage
with open('example.txt', 'rb') as f:
    reader = safe_readlines(f)
    for line in reader:
        print(line)
