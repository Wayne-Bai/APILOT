from PIL import Image, ImageDraw

def draw_rounded_rectangle(image_path, output_path, rectangle, fill_color, outline_color, radius):
    """
    Draws a rounded rectangle on an image.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to the output image.
        rectangle (tuple): Rectangle coordinates in the format (x0, y0, x1, y1).
        fill_color (tuple): Fill color in the format (R, G, B).
        outline_color (tuple): Outline color in the format (R, G, B).
        radius (int): Radius of the rounded rectangle.

    Returns:
        None
    """

    # Open the image
    img = Image.open(image_path)
    
    # Create a drawing context
    draw = ImageDraw.Draw(img)

    # Draw the rounded rectangle
    draw.rounded_rectangle(rectangle, fill=fill_color, outline=outline_color, width=2, radius=radius)

    # Save the output image
    img.save(output_path)


# Example usage
if __name__ == "__main__":
    image_path = "input.png"
    output_path = "output.png"
    rectangle = (50, 50, 300, 300)
    fill_color = (240, 230, 140)
    outline_color = (100, 100, 100)
    radius = 20
    
    draw_rounded_rectangle(image_path, output_path, rectangle, fill_color, outline_color, radius)
