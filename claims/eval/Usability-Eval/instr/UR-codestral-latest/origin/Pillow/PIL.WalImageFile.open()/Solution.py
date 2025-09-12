from PIL import Image
import struct

# Function to read WAL header
def read_wal_header(file):
    header = file.read(32)
    width, height = struct.unpack('<II', header[4:12])
    offsets = struct.unpack('<IIII', header[12:28])
    return width, height, offsets

# Function to load texture from WAL file
def load_texture(filename):
    with open(filename, 'rb') as file:
        width, height, offsets = read_wal_header(file)
        images = []
        for offset in offsets:
            file.seek(offset)
            image = Image.frombytes('P', (width, height), file.read())
            images.append(image)
        return images

# Load texture and display first image (highest level of detail)
filename = 'your_texture_file.wal'
textures = load_texture(filename)
textures[0].show()
