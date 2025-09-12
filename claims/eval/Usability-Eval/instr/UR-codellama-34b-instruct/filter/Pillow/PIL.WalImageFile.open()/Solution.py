
from PIL import Image

def load_texture(file):
    # Open the WAL file and extract the texture data
    with open(file, 'rb') as f:
        texture = f.read()

    # Create a PIL image from the texture data
    img = Image.frombytes('RGBA', (128, 128), texture)

    return img
