from PIL import Image, ImageDraw

def draw_rounded_rectangle(image, x, y, width, height, radius, fill_color, outline_color):
    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Draw the rounded rectangle
    draw.rounded_rectangle([(x, y), (x + width, y + height)], radius=radius, fill=fill_color, outline=outline_color)

    # Return the modified image
    return image
