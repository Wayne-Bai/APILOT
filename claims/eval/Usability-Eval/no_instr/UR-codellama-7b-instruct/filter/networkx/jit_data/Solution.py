
import json
from typing import List

def get_jit_json(nodes: List[str], edges: List[tuple]) -> dict:
    """
    Generates a JSON object with nodes and edges in JIT format.

    Args:
        nodes (List[str]): A list of node IDs.
        edges (List[tuple]): A list of edge tuples containing the source and target node IDs, respectively.

    Returns:
        dict: A JSON object with nodes and edges in JIT format.
    """
    data = {"nodes": [], "edges": []}
    for i, node in enumerate(nodes):
        data["nodes"].append({"id": i, "label": node})
    for edge in edges:
        source, target = edge
        data["edges"].append({"source": source, "target": target})
    return json.dumps(data)
