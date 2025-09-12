from PIL import Image

# Open the texture file
with open("texture.wal", "rb") as f:
    data = f.read()

# Extract the width and height of the texture
width = int.from_bytes(data[0x12:0x16], byteorder="big")
height = int.from_bytes(data[0x16:0x1a], byteorder="big")

# Extract the image data
image_data = data[0x20:]

# Create an image object from the image data
image = Image.frombytes("RGBA", (width, height), image_data)

# Save the image to a file
image.save("texture.png")
