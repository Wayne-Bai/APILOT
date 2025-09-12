from PIL import Image

def load_wal_texture(wal_file_path):
    with open(wal_file_path, 'rb') as wal_file:
        # Read the WAL file header
        name = wal_file.read(32).decode('utf-8').rstrip('\0')
        width = int.from_bytes(wal_file.read(4), 'little')
        height = int.from_bytes(wal_file.read(4), 'little')
        offsets = [int.from_bytes(wal_file.read(4), 'little') for _ in range(4)]
        next_name = wal_file.read(32).decode('utf-8').rstrip('\0')
        flags = int.from_bytes(wal_file.read(4), 'little')
        contents = int.from_bytes(wal_file.read(4), 'little')
        value = int.from_bytes(wal_file.read(4), 'little')

        # Read the palette data from the WAL file
        wal_file.seek(offsets[0])
        palette_data = wal_file.read(width * height)

        # Create an image from the palette data
        image = Image.new('P', (width, height))
        image.putdata(list(palette_data))

        # Load the palette from the WAL file
        wal_file.seek(256 * 3, 1)  # Skip the header and palette data
        palette = wal_file.read(256 * 3)
        image.putpalette(palette)

        return image

# Example usage
wal_texture = load_wal_texture('path_to_your_wal_file.wal')
wal_texture.show()
