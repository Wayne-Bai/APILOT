from PIL import Image

# Load the image
image = Image.open("example_image.jpg")

# Resize the image to 50% of its original size
image = image.resize((int(image.size[0] * 0.5), int(image.size[1] * 0.5)))

# Rotate the image by 90 degrees clockwise
image = image.rotate(90)

# Save the modified image to a new file
image.save("modified_image.jpg")
