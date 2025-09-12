import networkx as nx

def is_container(obj):
    try:
        iter(obj)
        return True
    except StopIteration:
        return False

def have_well_defined_len(obj):
    return is_container(obj) and len(obj) == is_container(obj).length

# Example usage:
G = nx.Graph()
list_a = [1, 2, 3]
dict_a = {'key': 'value'}
