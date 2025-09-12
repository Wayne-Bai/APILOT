from PIL import Image

def load_quake2_wal_texture(file_path):
    # Open the image file
    with Image.open(file_path) as img:
        # Convert the image to RGB if it's in RGBA mode
        if img.mode != 'RGB':
            img = img.convert('RGB')
        return img

# Example usage:
# Load a Quake2 WAL texture file
texture_image = load_quake2_wal_texture('path/to/your/texture.wal')
# Process or display the texture image as needed
