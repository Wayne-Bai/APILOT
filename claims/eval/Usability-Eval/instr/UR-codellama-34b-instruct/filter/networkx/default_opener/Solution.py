import networkx as nx

def open_file(filename):
    """Opens a file using the system's default program."""
    # Get the default application for opening files based on their extension
    default_app = nx.get_default_application()
    # Open the file with the default application
    nx.open_file(filename, default_app)
