from PIL import Image, ImageDraw

def draw_rounded_rectangle(image, xy, radius, fill=None, outline=None, width=1):
    """
    Draws a rounded rectangle on the given image.
    
    :param image: The image where the rectangle will be drawn.
    :param xy: A tuple of coordinates (x0, y0, x1, y1) defining the rectangle.
    :param radius: The radius of the corners.
    :param fill: Color to fill the rounded rectangle.
    :param outline: Color for the outline of the rounded rectangle.
    :param width: Width of the outline.
    """
    draw = ImageDraw.Draw(image)
    
    x0, y0, x1, y1 = xy
    # Draw the four quarter circles
    draw.pieslice([x0, y0, x0 + 2 * radius, y0 + 2 * radius], 180, 270, fill=fill, outline=outline, width=width)
    draw.pieslice([x1 - 2 * radius, y0, x1, y0 + 2 * radius], 270, 360, fill=fill, outline=outline, width=width)
    draw.pieslice([x1 - 2 * radius, y1 - 2 * radius, x1, y1], 0, 90, fill=fill, outline=outline, width=width)
    draw.pieslice([x0, y1 - 2 * radius, x0 + 2 * radius, y1], 90, 180, fill=fill, outline=outline, width=width)
    
    # Draw the four rectangular sides
    draw.rectangle([x0 + radius, y0, x1 - radius, y1], fill=fill, outline=outline, width=width)
    draw.rectangle([x0, y0 + radius, x1, y1 - radius], fill=fill, outline=outline, width=width)
    
    # Fill in the center
    draw.rectangle([x0 + radius, y0 + radius, x1 - radius, y1 - radius], fill=fill)

# Example Usage
image = Image.new("RGBA", (200, 200), (255, 255, 255, 0))
draw_rounded_rectangle(image, (20, 20, 180, 180), radius=20, fill=(255, 0, 0, 255), outline=(0, 0, 0, 255), width=2)

image.show()
