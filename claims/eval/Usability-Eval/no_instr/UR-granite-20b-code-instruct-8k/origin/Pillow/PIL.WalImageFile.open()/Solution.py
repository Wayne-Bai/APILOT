import PIL.Image

# Open the WAL file
with open("texture.wal", "rb") as f:
    wal_data = f.read()

# Extract the texture data
texture_data = wal_data[0x100:]

# Create an image from the texture data
texture_image = PIL.Image.frombytes("RGBA", (64, 64), texture_data)

# Save the image
texture_image.save("texture.png")
