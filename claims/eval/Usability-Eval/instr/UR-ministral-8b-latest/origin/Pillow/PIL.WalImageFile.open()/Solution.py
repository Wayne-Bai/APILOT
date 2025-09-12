from PIL import Image

def load_wal_texture(file_path):
    with open(file_path, 'rb') as f:
        wal_data = f.read()

    # Strip out the header (first 16 bytes)
    wal_data = wal_data[16:]

    width = int.from_bytes(wal_data[:2], byteorder='little')
    height = int.from_bytes(wal_data[2:4], byteorder='little')
    pixel_count = width * height * 8  # Since it's 8-bit per pixel

    # Extract pixel data from the WAL file
    pixel_data = wal_data[4:pixel_count + 4]

    # Create an empty Image object
    image = Image.new('RGBA', (width, height))

    # Flatten the pixel data into a list for individual pixel manipulation
    pixel_list = []
    for byte in pixel_data:
        pixel_list.append(int(~byte & 255))  # Quake2 uses color inverted

    # Populate the image with pixel values
    for x in range(width):
        for y in range(height):
            pixel = pixel_list[x * height + y]
            image.putpixel((x, y), (pixel, pixel, pixel, 255))

    return image

if __name__ == "__main__":
    texture_file = "example.wal"
    img = load_wal_texture(texture_file)
    img.show()
