from PIL import Image

# Sample 2-dimensional pixel data
# Here, we assume a grayscale image, where each value ranges from 0 (black) to 255 (white)
pixel_data = [
    [255, 0, 255, 0, 255],
    [0, 255, 0, 255, 0],
    [255, 0, 255, 0, 255],
    [0, 255, 0, 255, 0],
    [255, 0, 255, 0, 255]
]

# Create an image from this 2D list
# Dimensions of image
width, height = len(pixel_data[0]), len(pixel_data)
# Create a new image in 'L' mode (grayscale) and set the pixel data
image = Image.new('L', (width, height))
for y in range(height):
    for x in range(width):
        image.putpixel((x, y), pixel_data[y][x])

# Save or display the image
image.show()  # This will display the image to your default image viewer
# image.save('output_image.png')  # Optionally, save the image to a file
