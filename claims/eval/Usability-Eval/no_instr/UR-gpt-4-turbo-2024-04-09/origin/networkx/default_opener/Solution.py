import networkx as nx
import os

def open_file_with_default_program(filename):
    # Attempt to open the file with the default application
    try:
        os.startfile(filename)
    except AttributeError:
        # os.startfile is unavailable on non-Windows systems, use subprocess as an alternative
        import subprocess
        if 'darwin' in os.sys.platform:  # macOS
            subprocess.call(('open', filename))
        elif 'linux' in os.sys.platform:  # Linux
            subprocess.call(('xdg-open', filename))
        else:
            print("OS not supported for opening a file with the default program.")

# Example usage:
open_file_with_default_program("example.txt")
