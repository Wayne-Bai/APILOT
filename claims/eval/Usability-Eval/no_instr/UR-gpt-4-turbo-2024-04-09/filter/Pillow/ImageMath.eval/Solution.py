from PIL import Image, ImageChops

# Open the images
image1 = Image.open('image1.jpg')
image2 = Image.open('image2.jpg')

# Evaluate the expression: adding two images
result_image = ImageChops.add(image1, image2)

# Save the result
result_image.save('result.jpg')

# Optionally display the result using show (this will pop up the image using the default viewer)
result_image.show()
