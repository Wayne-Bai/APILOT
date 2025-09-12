
from PIL import Image
import numpy as np

# Load the image
image = Image.open("image.jpg")

# Define the expression to be evaluated
expression = "image - 0.5"

# Evaluate the expression
result = eval(expression)

# Save the result as a new image
Image.fromarray(result).save("output.jpg")
