import networkx as nx
import types

def is_iterator(obj):
    """
    Returns True if and only if the given object is an iterator object.
    
    Parameters:
    obj (object): The object to check.
    
    Returns:
    bool: True if the object is an iterator, False otherwise.
    """
    return isinstance(obj, type(df_iter)) or hasattr(obj, '__iter__') or isinstance(obj, types.GeneratorType)

# Create a networkx graph for demonstration
G = nx.Graph()
G.add_node("Node1")
G.add_node("Node2")

# Simulate a networkx graph iteration
for node in G.nodes():
    # Creating a simple custom iterator object
    class df_iter:
        def __iter__(self):
            self.iterate = iter([node])
            return self
    
        def __next__(self):
            return next(self.iterate)

    # Simulating an iterator object
    iter_obj = df_iter()

    # Checking if the `iter_obj` is an iterator
    print(is_iterator(iter_obj))  # Should print: True

    # Checking if the `G.nodes()` is an iterator
    print(is_iterator(G.nodes()))  # Should print: True

    # Checking if an integer is an iterator
    print(is_iterator(123))  # Should print: False

