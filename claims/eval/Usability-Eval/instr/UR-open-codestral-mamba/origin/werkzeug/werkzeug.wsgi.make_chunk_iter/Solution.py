from werkzeug.utils import secure_filename

def make_custom_iter(file_object, separator):
    chunk = file_object.read(separator)
    while chunk:
        yield chunk
        chunk = file_object.read(separator)

# Example usage:
# with open('largefile.txt', 'rb') as f:
#     for chunk in make_custom_iter(f, 1024):
#         process_chunk(chunk)
