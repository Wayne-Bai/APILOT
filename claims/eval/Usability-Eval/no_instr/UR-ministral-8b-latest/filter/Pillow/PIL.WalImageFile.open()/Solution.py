from PIL import Image

def load_wal_texture(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()

    if data[0] != 0x1:  # Check for the magic number 0x1 indicating WAL file
        return None

    width = data[4] + data[5] * 256  # Width of the texture
    height = data[8] + data[9] * 256  # Height of the texture

    offset = 12 + 24  # Skip past the version and name strings

    # Extract image data
    pixels = data[offset:offset + width * height * 3]
    pixels = bytes(pixels[i:i + 3] for i in range(0, len(pixels), 3))  # Convert to RGB format

    image = Image.frombytes('RGB', (width, height), pixels)
    return image

# Example usage:
wal_file_path = 'path/to/your/texture.wal'
texture_image = load_wal_texture(wal_file_path)
if texture_image:
    texture_image.show()
else:
    print("Failed to load WAL texture.")
