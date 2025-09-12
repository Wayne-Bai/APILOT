from PIL import Image, ImageDraw

def draw_rounded_rectangle(draw, xy, radius, fill=None, outline=None):
    # Create the points for the rounded rectangle
    x0, y0, x1, y1 = xy
    draw.rectangle([x0 + radius, y0, x1 - radius, y1], fill=fill, outline=outline)
    draw.rectangle([x0, y0 + radius, x1, y1 - radius], fill=fill, outline=outline)

    # Draw the corners
    draw.pieslice([x0, y0, x0 + 2 * radius, y0 + 2 * radius], 180, 270, fill=fill, outline=outline)
    draw.pieslice([x1 - 2 * radius, y0, x1, y0 + 2 * radius], 270, 360, fill=fill, outline=outline)
    draw.pieslice([x0, y1 - 2 * radius, x0 + 2 * radius, y1], 90, 180, fill=fill, outline=outline)
    draw.pieslice([x1 - 2 * radius, y1 - 2 * radius, x1, y1], 0, 90, fill=fill, outline=outline)

# Create an image
image = Image.new("RGB", (200, 100), "white")
draw = ImageDraw.Draw(image)

# Draw a rounded rectangle
draw_rounded_rectangle(draw, (20, 20, 180, 80), radius=20, fill="blue", outline="black")

# Save or show the image
image.show()
