from PIL import Image

def load_quake2_wal_texture(file_path):
    with open(file_path, 'rb') as file:
        # Read the header
        header = file.read(12)
        if header != b'QUAKEDW2':
            raise ValueError("Invalid Quake2 WAL file")

        # Read the texture dimensions
        width, height = struct.unpack('>II', file.read(8))

        # Read the texture data
        data = file.read()

        # Create a new image with the correct dimensions
        image = Image.new('RGBA', (width, height))

        # Paste the texture data into the image
        image.paste(Image.frombytes('RGBA', (width, height), data), (0, 0))

        return image
