import networkx as nx

# define a function to open a file using the system's default program
def open_file(filename):
    # get the path of the file
    filepath = os.path.realpath(filename)
    
    # use the subprocess module to open the file with its default program
    subprocess.run(['xdg-open', filepath])
