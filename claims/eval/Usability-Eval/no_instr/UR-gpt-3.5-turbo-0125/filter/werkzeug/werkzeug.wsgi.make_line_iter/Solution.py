
from werkzeug.wsgi import LineStream
from io import BytesIO

def process_input_stream(input_stream):
    # Wrap the input stream in a LineStream for safe line-based iteration
    stream = LineStream(input_stream)
    
    for line in stream:
        # Process each line from the input stream
        print(line)

# Example usage
input_data = b'Line 1\nLine 2\nLine 3\n'
input_stream = BytesIO(input_data)
process_input_stream(input_stream)
