from PIL import Image, ImageDraw

def draw_rounded_rectangle(image, bounding_box, radius, fill_color):
    draw = ImageDraw.Draw(image)
    x0, y0, x1, y1 = bounding_box
    
    # Draw the four corners
    draw.pieslice([(x0, y0), (x0 + 2 * radius, y0 + 2 * radius)], 180, 270, fill=fill_color)
    draw.pieslice([(x1 - 2 * radius, y0), (x1, y0 + 2 * radius)], 270, 360, fill=fill_color)
    draw.pieslice([(x0, y1 - 2 * radius), (x0 + 2 * radius, y1)], 90, 180, fill=fill_color)
    draw.pieslice([(x1 - 2 * radius, y1 - 2 * radius), (x1, y1)], 0, 90, fill=fill_color)
    
    # Draw the four sides
    draw.rectangle([(x0 + radius, y0), (x1 - radius, y0 + radius)], fill=fill_color)
    draw.rectangle([(x0 + radius, y1 - radius), (x1 - radius, y1)], fill=fill_color)
    draw.rectangle([(x0, y0 + radius), (x0 + radius, y1 - radius)], fill=fill_color)
    draw.rectangle([(x1 - radius, y0 + radius), (x1, y1 - radius)], fill=fill_color)
    
    # Draw the center rectangle
    draw.rectangle([(x0 + radius, y0 + radius), (x1 - radius, y1 - radius)], fill=fill_color)

# Example usage
image = Image.new("RGB", (200, 100), "white")
draw_rounded_rectangle(image, (20, 10, 180, 90), 10, "blue")
image.show()
