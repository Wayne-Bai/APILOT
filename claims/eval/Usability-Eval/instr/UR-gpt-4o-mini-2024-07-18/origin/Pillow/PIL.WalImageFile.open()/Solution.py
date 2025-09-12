from PIL import Image

def load_wal_texture(file_path):
    with open(file_path, 'rb') as f:
        # Read the WAL header
        header = f.read(32)
        texture_name = header[0:16].strip(b'\x00').decode('utf-8')
        width = int.from_bytes(header[16:18], 'little')
        height = int.from_bytes(header[18:20], 'little')
        offset = int.from_bytes(header[20:24], 'little')
        
        # Move the file pointer to the pixel data
        f.seek(offset)

        # Read pixel data
        raw_data = f.read(width * height * 3)  # 3 bytes per pixel (RGB)
        
        # Create an Image
        image = Image.frombuffer('RGB', (width, height), raw_data, 'raw', 'RGB', 0, 1)
        return texture_name, image

# Example usage
texture_name, image = load_wal_texture('path/to/your/texture.wal')
image.show()
