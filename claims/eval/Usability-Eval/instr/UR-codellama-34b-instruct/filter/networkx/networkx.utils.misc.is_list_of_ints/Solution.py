
import networkx as nx

def is_list_of_ints(my_list):
    """
    Returns True if the input is a list of integers, False otherwise.
    """
    return all(isinstance(x, int) for x in my_list)
