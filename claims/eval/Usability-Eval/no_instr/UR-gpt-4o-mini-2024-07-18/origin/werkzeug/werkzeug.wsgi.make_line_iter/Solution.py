from werkzeug.utils import secure_filename

def safe_line_iterator(input_stream):
    """
    Safely iterates over an input stream line by line.
    
    Args:
        input_stream: The input stream to read from.
        
    Yields:
        Each line from the input stream without the trailing newline.
    """
    try:
        for line in input_stream:
            yield line.strip()
    except Exception as e:
        print(f"An error occurred while reading the input stream: {e}")
