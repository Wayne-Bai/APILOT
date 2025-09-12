from PIL import Image
import struct

def read_wal_file(filepath):
    with open(filepath, 'rb') as file:
        # Read header data
        # struct.unpack() format:
        # 32s = 32 bytes string,
        # 4 integers for width, height, offsets of 4 mip maps
        data = file.read(100)  # first 100 bytes for header
        name, width, height, offset0, *_ = struct.unpack('<32siiiii16x', data)

        # Read the image data for the first mipmap level
        file.seek(offset0)
        image_data = file.read(width * height)

        # Create an image using PIL
        image = Image.frombytes('P', (width, height), image_data, 'raw')

        return image

# Usage
wal_texture_path = 'path_to_your_wal_file.wal'
image = read_wal_file(wal_texture_path)
image.show()  # Display the image to verify it
