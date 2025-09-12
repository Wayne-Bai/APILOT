from PIL import Image
import struct

def load_wal_file(filepath):
    # WAL file header format
    # name: 32 bytes
    # width, height: integer (4 bytes)
    # offsets: four integers (4 bytes each, mipmap levels)
    # next_name: 32 bytes
    # flags, contents, value: integers (4 bytes each)
    header_format = '32siiiiii32siii'
    header_length = struct.calcsize(header_format)

    # Open the WAL file in binary mode
    with open(filepath, 'rb') as file:
        # Read header data
        header_data = file.read(header_length)
        header = struct.unpack(header_format, header_data)
        
        name = header[0].decode('utf-8').strip('\x00')
        width = header[1]
        height = header[2]
        offset = header[3]  # offset to the main image data

        # Read main image data at offset
        file.seek(offset)
        image_data = file.read(width * height)  # each pixel is 1 byte

    # WAL textures are palettized; define a typical Quake2 palette or use a specific one
    # This is a simplified grayscale palette. In real applications, a game-specific palette is needed.
    palette = [(i, i, i) for i in range(256)]
    
    # Create an image with P mode for palettized and set the palette
    image = Image.frombytes('P', (width, height), image_data)
    image.putpalette([val for rgb in palette for val in rgb])

    return image

# Example usage:
# Replace 'path_to_wal_file.wal' with the actual path to the WAL file
wal_image = load_wal_file('path_to_wal_file.wal')
wal_image.show()  # Display the image
