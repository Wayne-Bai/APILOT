from PIL import Image

# Load the image
img = Image.open('image.jpg')

# Evaluate the image expression
result = eval(img, '(lambda x: x + 1)(3)')

# Print the result
print(result)
