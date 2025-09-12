from PIL import Image, ImageDraw

def draw_rounded_rectangle(image_width, image_height, corner_radius, fill_color):
    # Create a blank image with a white background
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    # Draw the rounded rectangle
    draw.rounded_rectangle(
        [(corner_radius, corner_radius), (image_width - corner_radius, image_height - corner_radius)],
        radius=corner_radius,
        fill=fill_color
    )

    # Save the image or display it
    image.show()

# Example usage
draw_rounded_rectangle(200, 100, 20, "blue")
