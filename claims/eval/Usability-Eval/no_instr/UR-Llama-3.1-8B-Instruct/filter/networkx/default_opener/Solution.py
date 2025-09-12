import networkx as nx
import os
import webbrowser

# Create a new directed graph
G = nx.DiGraph()

# Add nodes to the graph
nodes = ['file1.txt', 'file2.txt', 'file3.txt']
G.add_nodes_from(nodes)

# Add edges to the graph (in this case, to represent the action of opening each file)
for file in nodes:
    G.add_edge(file, 'open with default program')

# Create a dictionary mapping nodes to URLs representing their action
urls = {}
for file in nodes:
    url = f'file://{os.path.join(os.getcwd(), file)}'
    urls[file] = url

# Open each file in the system's default program
for file, url in urls.items():
    try:
        webbrowser.open(url)
        print(f'Opening {file} in default program...')
    except Exception as e:
        print(f'Failed to open {file}: {e}')
