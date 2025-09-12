from PIL import Image

def load_wal_texture(wal_file_path):
    with open(wal_file_path, 'rb') as wal_file:
        wal_file.seek(4)  # Skip the first 4 bytes (name)
        width = int.from_bytes(wal_file.read(4), 'little')
        height = int.from_bytes(wal_file.read(4), 'little')
        wal_file.seek(8, 1)  # Skip 8 bytes (offsets)
        palette_data = wal_file.read(256 * 3)
        image_data = wal_file.read(width * height)

    palette = []
    for i in range(0, len(palette_data), 3):
        r = palette_data[i]
        g = palette_data[i + 1]
        b = palette_data[i + 2]
        palette.append((r, g, b))

    img = Image.new('P', (width, height))
    img.putpalette(palette)
    img.putdata(image_data)
    img = img.convert('RGB')

    return img

# Example usage:
# wal_image = load_wal_texture('path_to_wal_file.wal')
# wal_image.show()
