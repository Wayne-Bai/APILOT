import networkx as nx

def is_int_list(my_list):
    try:
        for item in my_list:
            int(item)
        return True
    except ValueError:
        return False
