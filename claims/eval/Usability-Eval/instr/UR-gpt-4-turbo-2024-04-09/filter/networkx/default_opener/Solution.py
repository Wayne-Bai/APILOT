import networkx as nx
import os

def open_file_with_default_program(filename):
    try:
        os.startfile(filename)  # Works only on Windows
    except AttributeError:
        # For macOS and Linux, the os module does not include os.startfile()
        if sys.platform == "darwin":
            os.system(f"open {filename}")
        else:  # Assume it's Linux
            os.system(f"xdg-open {filename}")
