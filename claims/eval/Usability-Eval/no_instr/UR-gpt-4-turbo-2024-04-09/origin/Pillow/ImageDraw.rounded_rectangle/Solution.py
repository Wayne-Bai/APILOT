from PIL import Image, ImageDraw

def draw_rounded_rectangle(image_size, rect_size, corner_radius, fill_color, outline_color):
    """
    Draw an image with a rounded rectangle.

    :param image_size: Tuple of the form (width, height) for the size of the image
    :param rect_size: Tuple (x, y, x1, y1) defining the bounding box of the rounded rectangle
    :param corner_radius: Integer representing the radius of the corners
    :param fill_color: Color used to fill the rectangle
    :param outline_color: Color used for the outline of the rectangle
    :return: PIL.Image object with the drawn rounded rectangle
    """
    # Create a blank image
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    # Calculate rectangle boundaries
    left, top, right, bottom = rect_size

    # Draw the rounded rectangle using the ellipse (for corners) and rectangle primitives
    # Top-left corner
    draw.pieslice([left, top, left + 2 * corner_radius, top + 2 * corner_radius], 180, 270, fill=fill_color, outline=outline_color)
    # Top-right corner
    draw.pieslice([right - 2 * corner_radius, top, right, top + 2 * corner_radius], 270, 360, fill=fill_color, outline=outline_color)
    # Bottom-left corner
    draw.pieslice([left, bottom - 2 * corner_radius, left + 2 * corner_radius, bottom], 90, 180, fill=fill_color, outline=outline_color)
    # Bottom-right corner
    draw.pieslice([right - 2 * corner_radius, bottom - 2 * corner_radius, right, bottom], 0, 90, fill=fill_color, outline=outline_color)

    # Connect the corners with rectangles
    # Top and bottom
    draw.rectangle([left + corner_radius, top, right - corner_radius, top + corner_radius], fill=fill_color, outline=outline_color)
    draw.rectangle([left + corner_radius, bottom - corner_radius, right - corner_radius, bottom], fill=fill_color, outline=outline_color)
    # Left and right
    draw.rectangle([left, top + corner_radius, left + corner_radius, bottom - corner_radius], fill=fill_color, outline=outline_color)
    draw.rectangle([right - corner_radius, top + corner_radius, right, bottom - corner_radius], fill=fill_color, outline=outline_color)

    # Fill the center area
    draw.rectangle([left + corner_radius, top + corner_radius, right - corner_radius, bottom - corner_radius], fill=fill_color, outline=outline_color)

    return image

# Example usage
image_size = (300, 200)
rect_size = (50, 50, 250, 150)
corner_radius = 20
fill_color = "blue"
outline_color = "black"

rounded_rectangle_image = draw_rounded_rectangle(image_size, rect_size, corner_radius, fill_color, outline_color)
rounded_rectangle_image.show()
