import tensorflow as tf
import numpy as np

class Mesh:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.vertices = self._generate_vertices(dimensions)
        self.indices = self._generate_indices(dimensions)

    def _generate_vertices(self, dimensions):
        vertices = []
        for i in range(dimensions[0]):
            row = []
            for j in range(dimensions[1]):
                for k in range(dimensions[2]):
                    row.append([i, j, k])
            vertices.append(row)
        return np.array(vertices)

    def _generate_indices(self, dimensions):
        indices = []
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                for k in range(dimensions[2]):
                    for l in range(dimensions[2]):
                        indices.append([
                            i * dimensions[1] * dimensions[2] + j * dimensions[2] + k,
                            i * dimensions[1] * dimensions[2] + j * dimensions[2] + l,
                            i * dimensions[1] * dimensions[2] + j * dimensions[2] + k,
                            i * dimensions[1] * dimensions[2] + j * dimensions[2] + l
                        ])
        return np.array(indices)

# Example usage
mesh = Mesh([5, 5, 5])
print("Vertices:")
print(mesh.vertices)
print("Indices:")
print(mesh.indices)
