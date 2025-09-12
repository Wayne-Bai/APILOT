import networkx as nx
from collections.abc import Iterator

def is_iterator_object(obj):
    return isinstance(obj, Iterator)
