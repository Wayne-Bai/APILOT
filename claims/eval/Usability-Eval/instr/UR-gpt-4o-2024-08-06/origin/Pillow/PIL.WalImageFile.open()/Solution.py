from PIL import Image
import struct

def load_wal_texture(file_path):
    with open(file_path, 'rb') as f:
        # Read header information
        name = f.read(32).decode('utf-8').rstrip('\x00')
        width, height = struct.unpack('ii', f.read(8))
        offsets = struct.unpack('iiii', f.read(16))
        
        # Skip the remainder of the header
        f.read(40 + 4 * 256)
        
        # Read the image data starting at the first mipmap offset
        f.seek(offsets[0])
        data = f.read(width * height)
        
        # Convert the data to an image (assume the palette is in a separate section)
        palette = []
        for i in range(256):
            palette.extend(f.read(3))
            f.read(1)  # skip padding byte

        image = Image.frombytes('P', (width, height), data)
        image.putpalette(palette)
        
        return image

# Example usage (ensure 'example.wal' is a valid WAL texture file path):
# texture_image = load_wal_texture('example.wal')
# texture_image.show()  # This will open the texture image
