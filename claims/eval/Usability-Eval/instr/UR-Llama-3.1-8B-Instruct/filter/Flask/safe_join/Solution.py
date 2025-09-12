from flask import Flask, url_for
import os

app = Flask(__name__)

# We'll define a function to join path components safely
def join_path_components(base_dir, *components):
    """
    Join zero or more untrusted path components to a base directory.
    
    This function aims to prevent path traversal attacks by ensuring that the joined
    path does not escape the base directory.

    :param base_dir: The base directory to join with.
    :param components: Zero or more path components to join.
    :returns: The joined path.
    """
    # Normalize the base directory to remove any redundant separators
    normalized_base_dir = os.path.normpath(base_dir)
    
    # Initialize the joined path with the normalized base directory
    joined_path = normalized_base_dir
    
    # Iterate over each component to add to the joined path
    for component in components:
        # Use os.path.join to join the component to the existing joined path
        # This will correctly handle cases where the component is Windows-style or Unix-style
        joined_path = os.path.join(joined_path, component)
    
    # Normalize the joined path again to eliminate any redundant separators
    joined_path = os.path.normpath(joined_path)
    
    # Ensure that the joined path is still within the base directory
    if not os.path.join(normalized_base_dir, joined_path) == joined_path:
        raise ValueError("Escaped the base directory")
    
    return joined_path

# Define a route that showcases the join_path_components function
@app.route("/join-path/<path:components>")
def join_path(components):
    """Join zero or more path components to a base directory."""
    base_dir = "/home/user"
    joined_path = join_path_components(base_dir, components)
    return f"The joined path is: {url_for('static', filename='join_path.jpg', _external=True)} is not our target. The actual result is Path: {joined_path}"

if __name__ == "__main__":
    app.run(debug=True)
