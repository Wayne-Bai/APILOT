from PIL import Image
import struct

def load_wal_texture(file_path):
    # WAL header structure: 32 bytes for name, 8 * 4 bytes each for width/height and offsets
    header_format = '32s8I'
    header_size = struct.calcsize(header_format)

    with open(file_path, 'rb') as file:
        # Read header data
        header_data = file.read(header_size)
        name, width, height, *_ = struct.unpack(header_format, header_data)
        width = width or 1
        height = height or 1

        # Calculate size of the mip level 0
        mip_size = width * height

        # Read the palette
        file.seek(-768, 2)  # Move to the start of the palette section at the end of the file
        palette_data = file.read(768)
        palette = [
            (palette_data[i], palette_data[i+1], palette_data[i+2])
            for i in range(0, len(palette_data), 3)
        ]

        # Read the pixel data of mip level 0
        file.seek(header_size)
        pixel_data = file.read(mip_size)
        
        # Create an image from pixel data
        image = Image.new("P", (width, height))
        image.putpalette(sum(palette, ()))
        image.frombytes(pixel_data)

    return image

# Example usage:
# img = load_wal_texture("path_to_texture.wal")
# img.show()
