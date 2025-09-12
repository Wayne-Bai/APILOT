from PIL import Image

def load_texture_from_wal(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        # Skip the header, which is 64 bytes long for Quake II WAL files
        data = data[64:]
        # Read the width and height of the image
        width, height = struct.unpack('HH', data[:4])
        # Create a PIL image from the loaded data
        img = Image.frombytes('P', (width, height), data)

    return img
