from PIL import Image
import struct

def load_wal_texture(file_path):
    # Open the WAL file in binary mode
    with open(file_path, 'rb') as file:
        # Read the file header
        file_header = file.read(16)
        
        # Check if the file is a Quake2 WAL texture file
        if file_header[0:4]!= b'WAL ':
            raise ValueError("The file is not a Quake2 WAL texture file.")
        
        # Read the width and height of the texture
        width, height = struct.unpack('II', file.read(8))
        
        # Read the number of mipmaps and the palette size
        num_mipmaps, palette_size = struct.unpack('II', file.read(8))
        
        # Seek to the start of the palette data
        file.seek(16 + 8 + 8 + 16)
        
        # Read the palette data
        palette_data = file.read(palette_size * 3)
        
        # Create a palette from the palette data
        palette = []
        for i in range(palette_size):
            palette.extend(struct.unpack('BBB', palette_data[i*3:(i+1)*3]))
        
        # Create a new image with the palette
        image = Image.new('P', (width, height))
        image.putpalette(palette)
        
        # Seek to the first mipmap data
        file.seek(16 + 8 + 8 + 16 + palette_size * 3)
        
        # Read the first mipmap data
        mipmap_data = file.read(width * height)
        
        # Load the mipmap data into the image
        image.putdata(mipmap_data)
        
        return image

# Example usage:
texture_image = load_wal_texture('texture.wal')
texture_image.show()
