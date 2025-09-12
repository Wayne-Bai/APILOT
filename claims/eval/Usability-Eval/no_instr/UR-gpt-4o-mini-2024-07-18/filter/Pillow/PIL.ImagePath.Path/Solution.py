from PIL import Image, ImageDraw

# Example function to create and manipulate a 2D vector using Pillow

def create_image_with_vector(width, height, vector_start, vector_end):
    # Create a new image with white background
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Draw the 2D vector as a line on the image
    draw.line([vector_start, vector_end], fill="black", width=2)

    # Save the image to a file
    image.save("vector_image.png")
    print("Image saved as 'vector_image.png'")

# Example usage
create_image_with_vector(400, 400, (50, 150), (350, 300))
