import networkx as nx

def is_iterator(object_to_test):
    return isinstance(object_to_test, (list, tuple, set, dict, range, bytearray, memoryview))
