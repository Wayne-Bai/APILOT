from PIL import Image

def load_texture(file_path):
    try:
        img = Image.open(file_path)
        img.load()
        return img
    except IOError:
        print(f"Error: Could not open or load image file '{file_path}'")
        return None

# Usage
texture_path = "path/to/your/texture.wal"
texture = load_texture(texture_path)
if texture:
    texture.show()
else:
    print("Error loading texture")
