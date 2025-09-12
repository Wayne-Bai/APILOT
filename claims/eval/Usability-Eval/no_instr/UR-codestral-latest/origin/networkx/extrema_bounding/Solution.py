import networkx as nx

# Assuming G is your graph
# If G is not defined, you should replace this line with your graph definition or loading code
# G = nx.some_graph_generating_function()

# Compute the diameter
diameter = nx.diameter(G)
print(f"The diameter of the graph is: {diameter}")

# Compute the eccentricity of each node
eccentricity = nx.eccentricity(G)
print(f"The eccentricity of each node is: {eccentricity}")
