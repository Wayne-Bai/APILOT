from PIL import Image

def load_quake2_wal_texture(file_path):
    with open(file_path, 'rb') as file:
        header = file.read(12)
        if header != b'WalHeader':
            raise ValueError("Invalid file format")

        width, height = struct.unpack('>II', file.read(8))
        format = file.read(1)[0]
        bits_per_pixel = struct.unpack('>B', file.read(1))[0]

        if format not in (1, 2, 3, 4):
            raise ValueError("Unsupported format")

        if bits_per_pixel not in (8, 16, 24, 32):
            raise ValueError("Unsupported bits per pixel")

        if format == 1:
            pixel_data = [struct.unpack('>H', file.read(2))[0] for _ in range(width * height)]
        elif format == 2:
            pixel_data = [struct.unpack('>h', file.read(2))[0] for _ in range(width * height)]
        elif format == 3:
            pixel_data = [struct.unpack('>B', file.read(1))[0] for _ in range(width * height * 3)]
        elif format == 4:
            pixel_data = [struct.unpack('>b', file.read(1))[0] for _ in range(width * height * 4)]

        image = Image.new('RGB', (width, height))
        image.putdata(pixel_data)

        return image
