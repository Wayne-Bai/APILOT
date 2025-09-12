from PIL import Image
import struct

def load_wal_texture(file_path):
    with open(file_path, 'rb') as f:
        # Read the header
        header = f.read(16)
        texture_name = header[0:16].decode('utf-8').rstrip('\0')
        width, height = struct.unpack('ii', header[16:24])

        # Read the pixel data
        size = width * height * 3  # 3 bytes per pixel (RGB)
        pixel_data = f.read(size)

        # Convert pixel data to Image
        image = Image.new('RGB', (width, height))
        image_data = []

        for i in range(width * height):
            r = pixel_data[i * 3]
            g = pixel_data[i * 3 + 1]
            b = pixel_data[i * 3 + 2]
            image_data.append((r, g, b))

        image.putdata(image_data)
        return texture_name, image

# Example usage
# texture_name, texture_image = load_wal_texture('path/to/your/texture.wal')
# texture_image.show()
