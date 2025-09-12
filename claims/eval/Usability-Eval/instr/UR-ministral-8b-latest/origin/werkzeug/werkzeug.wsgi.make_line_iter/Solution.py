from werkzeug import _internal as _wf
import io

def safe_iter_lines(input_stream):
    iterator = _wf._iter_for_lines_iter(input_stream)
    for line in iterator:
        yield line

# Example usage:
if __name__ == "__main__":
    example_text = b"Line 1\nLine 2\nLine 3"

    with io.BytesIO(example_text) as input_stream:
        for line in safe_iter_lines(input_stream):
            print(line.decode('utf-8'))
