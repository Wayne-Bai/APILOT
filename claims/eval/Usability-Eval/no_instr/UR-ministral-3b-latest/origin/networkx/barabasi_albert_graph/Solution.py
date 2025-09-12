import networkx as nx
import random

G = nx.ErdosRenyiGraph(nodelist=list(range(100)),EA=0.01)
