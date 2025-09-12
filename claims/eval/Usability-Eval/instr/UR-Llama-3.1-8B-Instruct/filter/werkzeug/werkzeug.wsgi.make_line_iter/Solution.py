from werkzeug.datastructures import CombinedMultiDict
from werkzeug.http import parse_qs

def safely_iterate_input(input_stream):
    """
    This function safely iterates line-based over an input stream.
    
    Args:
        input_stream (str or file): Input stream to iterate over.
        
    Yields:
        str: Each line in the input stream.
    """
    
    if hasattr(input_stream,'read'):
        # If input stream is a file-like object, read it line by line
        while True:
            line = input_stream.readline()
            if line:
                yield line.decode('utf-8')
            else:
                break
    else:
        # If input stream is a string, split it line by line
        if isinstance(input_stream, CombinedMultiDict):
            lines = parse_qs(input_stream.get('input'))
        else:
            lines = parse_qs(input_stream)
        for line in lines.get('input', []):
            yield line
