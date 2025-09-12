import tensorflow as tf
class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = {}

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.edges:
            self.edges[vertex1] = {}
        self.edges[vertex1][vertex2] = weight

class PolymorphicGraph(Graph):
    def __init__(self):
        super().__init__()

    def add_vertex(self, vertex):
        super().add_vertex(vertex)

    def add_edge(self, vertex1, vertex2, weight):
        super().add_edge(vertex1, vertex2, weight)

    def get_shortest_path(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            raise ValueError("Invalid start or end vertex")
        visited = set()
        queue = [(start, [start])]
        while queue:
            current, path = queue.pop(0)
            if current == end:
                return path
            if current not in visited:
                visited.add(current)
                for neighbor, weight in self.edges[current].items():
                    queue.append((neighbor, path + [neighbor]))
        raise ValueError("No path found between start and end vertices")

g = PolymorphicGraph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edge("A", "B", 2)
g.add_edge("B", "C", 3)
g.add_edge("C", "D", 1)
print(g.get_shortest_path("A", "D"))
