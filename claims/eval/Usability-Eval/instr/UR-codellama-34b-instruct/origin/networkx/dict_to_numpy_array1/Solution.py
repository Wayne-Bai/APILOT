import networkx as nx

# create a sample dictionary of numbers
my_dict = {1: 'one', 2: 'two', 3: 'three'}

# convert the dictionary to a 1D NumPy array with optional mapping
my_array = nx.convert_dict_to_numpy(my_dict, map_fn=lambda x: int(x))

print(my_array) # output: [1 2 3]
