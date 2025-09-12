from flask import Flask, safe_join
from pathlib import Path

app = Flask(__name__)

def safe_path_join(base_dir, *paths):
    """
    Safely join zero or more untrusted path components to a base directory.
    
    Args:
    base_dir (str): The base directory to join paths to.
    *paths (str): Zero or more untrusted path components.
    
    Returns:
    str: The joined path.
    """
    return safe_join(base_dir, *paths)

# Example usage:
base_dir = '/home/user'

# If the path is absolute or attempts to escape the base directory, it will be ignored
path1 = safe_path_join(base_dir, '/etc/passwd')
path2 = safe_path_join(base_dir, '../../../../etc/passwd')

# The path is appended to the base directory
path3 = safe_path_join(base_dir, 'public', 'uploads', 'image.jpg')

print(Path(path1).resolve())
print(Path(path2).resolve())
print(Path(path3).resolve())
