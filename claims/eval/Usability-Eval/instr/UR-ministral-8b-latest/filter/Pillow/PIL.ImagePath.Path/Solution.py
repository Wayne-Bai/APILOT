from PIL import Image

# Load an existing image
image = Image.open('path_to_image.jpg')

# Create a款 empty image
new_image = Image.new('RGB', image.size, color = (255, 255, 255))

# Create a款 blank image with a transparent background
blank_image = Image.new('RGBA', image.size, color = (0, 0, 0, 0))

# Get the image data
image_data = image.load()

# Iterate over each pixel
for x in range(image.width):
    for y in range(image.height):
        r, g, b = image_data[x, y]

        # Convert to vector
        vec = list(map(lambda c: c / 255, [r, g, b]))

        # Do something with the vector
        # For example, add a constant vector to each pixel
        new_vec = [c + 0.1 for c in vec]
        new_image.load()[x, y] = tuple(map(int, new_vec))

# Save the new image
new_image.save('path_to_new_image.jpg')
