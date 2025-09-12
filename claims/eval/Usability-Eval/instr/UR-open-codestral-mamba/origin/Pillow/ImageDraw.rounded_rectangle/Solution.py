from PIL import Image, ImageDraw

def draw_rounded_rectangle(image, bounds, radius, outline, thickness):
    """Draw a rounded rectangle using the ImageDraw module."""

    x0, y0, x1, y1 = bounds

    # Adjust width and height
    width = x1 - x0
    height = y1 - y0

    # Create a mask with rounded corners and draw it on the image
    mask = Image.new('L', (width, height))
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, width, height], radius, fill=255)
    image.paste(outline, [x0, y0, x1, y1], mask)

    return image

# Example usage:
image = Image.new('RGB', (200, 100), color='white')
draw_rounded_rectangle(image, (10, 10, 90, 90), 10, 'black', 2)
image.save('rounded_rectangle.png')
