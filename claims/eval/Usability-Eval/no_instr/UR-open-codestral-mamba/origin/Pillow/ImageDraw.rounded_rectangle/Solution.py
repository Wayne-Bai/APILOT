from PIL import Image, ImageDraw, ImageOps

def draw_rounded_rectangle(image, xy, radius, fill=None, outline=None, width=1):
    """Draw a rounded rectangle

    Possible options for the fill element are:
      * a string naming a color (e.g. 'red')
      * an RGB tuple (e.g. (255, 0, 0))
      * a floating point value 0.0 (completely transparent) to 1.0 (completely opaque)
      * None (completely transparent)

    Possible options for the outline element are:
      * a string naming a color (e.g. 'red')
      * an RGB tuple (e.g. (255, 0, 0))
      * None (completely transparent)

    Args:
        image: Image to draw on.
        xy: Sequence [(x1, y1), (x2, y2)], (upper left, lower right).
        radius: Define the radius for rounded corners.
        fill: Color to fill the shape with.
        outline: Color to outline the shape with.
        width: Defines outline thickness.
    """
    # Create a blank mask with alpha
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle([x1, y1, x2, y2], radius, fill=255)
    if outline is not None:
        mask_outline = ImageOps.expand(mask, width, outline)
        mask = Image.alpha_composite(mask, mask_outline)
    image.paste(image, (x1, y1), mask)

    return image

# Example usage
image = Image.new('RGB', (500, 500), 'white')
xy = (50, 50, 450, 450)
radius = 30
fill = (255, 0, 0)  # RGB for red
outline = 'black'
width = 5

draw_rounded_rectangle(image, xy, radius, fill, outline, width)

# Save the image
image.save('rounded_rectangle.png')
