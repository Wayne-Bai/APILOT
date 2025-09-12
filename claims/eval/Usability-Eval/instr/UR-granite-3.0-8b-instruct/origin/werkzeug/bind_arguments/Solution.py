from werkzeug.utils import secure_filename

def process_file(file):
    # Bind the arguments provided into a dict
    args = {
        'file': file,
        'filename': secure_filename(file.filename),
        # Add more arguments as needed
    }

    # Process the file using the arguments
    # ...

    return processed_file
