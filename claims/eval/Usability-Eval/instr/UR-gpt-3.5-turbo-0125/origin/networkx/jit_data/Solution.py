
import networkx as nx

def jit_json_data(G):
    jit_data = {"nodes": [], "edges": []}
    
    for node in G.nodes(data=True):
        jit_node = {"id": node[0], "data": node[1]}
        jit_data["nodes"].append(jit_node)
        
    for edge in G.edges(data=True):
        jit_edge = {"source": edge[0], "target": edge[1], "data": edge[2]}
        jit_data["edges"].append(jit_edge)
        
    return jit_data
