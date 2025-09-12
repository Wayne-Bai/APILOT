from PIL import Image, ImageDraw

# Function to create a simple image with vector drawing
def create_vector_image():
    # Create a new white image
    image_size = (200, 200)
    image = Image.new('RGB', image_size, 'white')

    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # Draw a simple rectangle
    top_left = (50, 50)
    bottom_right = (150, 150)
    draw.rectangle([top_left, bottom_right], outline='black', fill='blue')

    # Draw a line
    draw.line((0, 0) + image_size, fill='red', width=3)

    # Draw an ellipse
    draw.ellipse([(40, 80), (160, 120)], outline='green', fill='yellow')

    # Save the image
    image.save('vector_image.png')

# Create a vector image
create_vector_image()
