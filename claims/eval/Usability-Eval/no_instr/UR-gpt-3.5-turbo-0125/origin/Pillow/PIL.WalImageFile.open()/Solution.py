
from struct import unpack

def load_wal_texture(file_path):
    with open(file_path, 'rb') as file:
        # Skip the first 4 bytes which are the magic number
        file.seek(4)

        # Read the width and height of the texture
        width = unpack('i', file.read(4))[0]
        height = unpack('i', file.read(4))[0]

        # Seek to the first offset table entry
        file.seek(40)

        # Read the texture data
        texture_data = bytearray()
        for _ in range(width * height):
            index = unpack('B', file.read(1))[0]
            texture_data.extend([index, index, index, 255])

    # Create a new image from the texture data
    from PIL import Image

    texture_image = Image.new('RGBA', (width, height))
    texture_image.putdata(texture_data)

    return texture_image
