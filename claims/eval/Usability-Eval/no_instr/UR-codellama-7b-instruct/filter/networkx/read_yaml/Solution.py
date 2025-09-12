
import yaml
from networkx import Graph

with open('graph.yaml') as f:
    G = yaml.load(f, Loader=yaml.FullLoader)
