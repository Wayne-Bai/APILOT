from PIL import Image

# Open an image file
img = Image.open('path_to_your_image.jpg')

# Convert the image to grayscale
img = img.convert('L')

# Get the pixel data of the image
pixels = img.load()

# Print the pixel data
for i in range(img.size[0]):
    for j in range(img.size[1]):
        print(pixels[i,j])
