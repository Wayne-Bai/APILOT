
from PIL import Image

# Function to load texture from a Quake2 WAL texture file
def load_texture_from_wal_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()

    offset = data.find(b'WAL')
    width = int.from_bytes(data[offset + 12:offset + 14], byteorder='little')
    height = int.from_bytes(data[offset + 14:offset + 16], byteorder='little')
    raw_data = data[offset + 40:]

    image = Image.frombytes('P', (width, height), raw_data)
    
    return image

# Example usage
file_path = 'example.wal'
texture_image = load_texture_from_wal_file(file_path)
texture_image.save('output.png')
