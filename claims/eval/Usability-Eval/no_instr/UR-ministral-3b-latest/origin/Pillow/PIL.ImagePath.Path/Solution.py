import PIL.Image as Image

# Example of manipulating an image to analyze its vector data
im = Image.open('example.png')
pixels = im.load()

# Get the dimensions of the image
width, height = im.size

# Print pixel vectors for a small piece of the image
for y in range(0, height, 20):  # step of 20
    for x in range(0, width, 20):  # step of 20
        pixel = pixels[x, y]
        print(pixel)
