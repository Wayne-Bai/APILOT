import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a function to safely join paths
def safe_join(directory, *paths):
    """Join one or more untrusted path components to a base directory.
    
    :param directory: The trusted base directory.
    :param paths: One or more untrusted path components.
    
    Raises:
        ValueError: If the combined path would escape the base directory.
    """
    abs_directory = os.path.abspath(directory)
    base_directory = os.path.normpath(abs_directory)
    words = filter(None, paths)

    # Join the base directory and untrusted paths
    for word in words:
        drive, word = os.path.splitdrive(word)
        invalid_levels = 0
        while os.path.sep in word:
            drive, word = os.path.splitdrive(word)
        while word and word!= os.path.curdir:
            if word == os.path.pardir:
                invalid_levels += 1
                word, _ = os.path.splitdrive(word)
            else:
                invalid_levels = 0
            word, _ = os.path.splitdrive(word)
        if invalid_levels > len(base_directory.split(os.path.sep)):
            raise ValueError(f"Path {paths} escapes the base directory {directory}")

        abs_path = os.path.abspath(os.path.join(base_directory, *paths))
        base_path = os.path.normpath(abs_path)
        if not base_path.startswith(abs_directory):
            raise ValueError(f"Path {paths} escapes the base directory {directory}")
        return base_path
    return base_directory


@app.route('/join', methods=['POST'])
def join_path():
    data = request.get_json()
    if 'directory' not in data or 'paths' not in data:
        return jsonify({'error': 'Missing required parameters'}), 400
    
    directory = data['directory']
    paths = data['paths']

    try:
        joined_path = safe_join(directory, *paths)
        return jsonify({'result': joined_path}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
