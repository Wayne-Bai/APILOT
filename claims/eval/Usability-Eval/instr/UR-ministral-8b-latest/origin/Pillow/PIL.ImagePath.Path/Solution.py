import numpy as np
from PIL import Image, ImageDraw

# Function to create an image using a 2D vectorili matrix
def create_image_from_matrix(matrix, width, height):
    image_array = np.array(matrix)
    image = Image.fromarray(image_array.astype(np.uint8), 'L')
    return image

# Function to create an image using a list of edges
def create_image_from_edges(edges, width, height):
    image = Image.new('L', (width, height))
    draw = ImageDraw.Draw(image)
    for edge in edges:
        draw.line(edge, fill=255)
    return image

# Example usage:
matrix = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
edges = [[(x, y), (x+1, y+1)] for x in range(100) for y in range(100)]
image_matrix = create_image_from_matrix(matrix, 100, 100)
with open('matrix_image.png', 'wb') as f:
    image_matrix.save(f)

image_edges = create_image_from_edges(edges, 100, 100)
with open('edges_image.png', 'wb') as f:
    image_edges.save(f)
