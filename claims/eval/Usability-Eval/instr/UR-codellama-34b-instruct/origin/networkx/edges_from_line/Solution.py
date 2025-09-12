
import networkx as nx
from shapely.geometry import LineString

# Load the GeoJSON file
with open("example.geojson") as f:
    data = json.load(f)

# Create a NetworkX graph from the GeoJSON data
G = nx.Graph()
for feature in data["features"]:
    if feature["geometry"]["type"] == "LineString":
        coords = feature["geometry"]["coordinates"]
        G.add_edge(coords[0], coords[-1])
