from PIL import Image, ImageDraw

def draw_rounded_rectangle(image, rect, radius, color):
    """
    Draws a rounded rectangle on the given image.

    Parameters:
        image (Image): The PIL Image object to draw on.
        rect (tuple): The rectangle bounds (x1, y1, x2, y2).
        radius (int): The radius of the corners of the rectangle.
        color (tuple or str): The color to fill the rectangle.
    """
    x1, y1, x2, y2 = rect
    draw = ImageDraw.Draw(image)

    # Draw the rectangle with rounded corners
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=color)
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=color)
    draw.pieslice([x1, y1, x1 + 2 * radius, y1 + 2 * radius], 180, 270, fill=color)
    draw.pieslice([x2 - 2 * radius, y1, x2, y1 + 2 * radius], 270, 360, fill=color)
    draw.pieslice([x1, y2 - 2 * radius, x1 + 2 * radius, y2], 90, 180, fill=color)
    draw.pieslice([x2 - 2 * radius, y2 - 2 * radius, x2, y2], 0, 90, fill=color)

# Create an image with a white background
image_size = (300, 200)
background_color = (255, 255, 255)
image = Image.new("RGB", image_size, background_color)

# Define the rectangle specs and color
rect_position = (50, 50, 250, 150)
radius = 20
color = (100, 100, 255)

# Draw the rounded rectangle
draw_rounded_rectangle(image, rect_position, radius, color)

# Save the image
image.save("rounded_rectangle.png")
image.show()
