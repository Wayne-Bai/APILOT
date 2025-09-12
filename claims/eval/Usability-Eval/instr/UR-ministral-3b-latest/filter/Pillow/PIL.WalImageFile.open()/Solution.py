from PIL import Image
import sys

# Check if the correct number of arguments are provided
if len(sys.argv) != 3:
    print("Usage: python image_to_png.py <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

def load_wal(input_file):
    color_model = None
    with open(input_file, "rb") as f:
        # Read the file in bytes
        data = f.read()

        # Find the starting position of the image data
        image_data_start = data.find(b"wall_") + len("wall")
        if image_data_start == -1:
            print(f"Invalid WAL file format. Couldn\'t find 'wall' in file.")
            sys.exit(1)

        # Find the size of the image data
        image_data_size = data.find(b"\n\n", image_data_start)
        image_data = data[image_data_start:image_data_size]

        # Check if the image data ends with a newline
        if not image_data.endswith(b"\n"):
            image_data = image_data.rstrip(b"\n")

        # Start of the color model header
        color_model_start = image_data.find(b"Image Data")
        if color_model_start != -1:
            color_model = image_data[color_model_start:].split(b"\n")[0]

            # Total number of bytes
            total_bytes = len(image_data) - len(color_model.rstrip(b"\n"))
            width = int(total_bytes / (color_model.rstrip(b"\n").decode().split()[1]))
            height = int(total_bytes / (color_model.rstrip(b"\n").decode().split()[1]) * 0.25)

            image_width = int(width / 2)
            image_height = int(height / 2)

            # Convert the image data to a PIL Image
            image_data_bytes = base64.b64decode(image_data.encode())
            image = Image.frombytes("P", (image_width, image_height), image_data_bytes)
            return image

    print(f"Error reading or processing file {input_file}")
    sys.exit(1)

image = load_wal(input_file)
image.show()
image.save(output_file, 'PNG')
