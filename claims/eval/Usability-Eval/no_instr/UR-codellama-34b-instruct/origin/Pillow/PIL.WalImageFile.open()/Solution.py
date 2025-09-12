import os
from PIL import Image
from io import BytesIO

def load_texture(file_path):
    # Load the WAL texture file
    with open(file_path, 'rb') as wal_file:
        # Read the header of the WAL file
        header = wal_file.read(64)
        width, height, mipmaps = struct.unpack('>HHB', header[:8])
        data_offset = struct.unpack('>I', header[12:16])[0]
        # Load the texture data
        wal_file.seek(data_offset)
        data = wal_file.read()
    # Create a PIL image object from the texture data
    im = Image.frombytes('RGB', (width, height), data, 'raw')
    # Apply any necessary transformations to the image
    if mipmaps > 0:
        for i in range(mipmaps):
            im = im.reduce(2 ** (i + 1))
    return im
