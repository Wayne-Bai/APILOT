from PIL import Image, ImageDraw, ImageOps

def draw_rounded_rectangle(image_path, output_path, top_left, bottom_right, width, height, corner_radius):
    # Load the image
    image = Image.open(image_path)

    # Draw on the image
    draw = ImageDraw.Draw(image)

    # Calculate corner coordinates
    top_left = (top_left[0], top_left[1])
    bottom_right = (bottom_right[0], bottom_right[1])
    top_right = (bottom_right[0] - width, bottom_right[1])
    bottom_left = (bottom_left[0], top_left[1])

    # Draw rounded rectangle
    draw.rounded_rectangle([top_left, bottom_right], width, height, float(corner_radius), fill="white")

    # Save the image
    image.save(output_path)

# Example usage
draw_rounded_rectangle("input_image.jpg", "output_image.jpg", (50, 50), (300, 300), 40, 40, 20)
