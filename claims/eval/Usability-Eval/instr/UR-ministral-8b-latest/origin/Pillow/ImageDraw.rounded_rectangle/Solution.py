from PIL import Image, ImageDraw

def draw_rounded_rectangle(image_path, output_path, width, height, radius, outline, fill):
    # Open an image file
    image = Image.open(image_path)
    drawer = ImageDraw.Draw(image)

    # Define the coordinates of the rectangle
    x1, y1 = 50, 50
    x2, y2 = x1 + width, y1 + height

    # Draw the rounded rectangle
    drawer.arc((x1 + radius, y1, x2 - radius, y1), start=180, end=270, fill=fill)
    drawer.arc((x1, y1 + radius, x1 + radius, y2 - radius), start=90, end=0, fill=fill)
    drawer.arc((x2 - radius, y1, x2, y2 - radius), start=270, end=180, fill=fill)
    drawer.arc((x1, y2 - radius, x2, y2), start=0, end=90, fill=fill)

    drawer.rectangle((x1, y1, x2, y1), fill=fill, outline=outline)
    drawer.rectangle((x1, y1 + radius, x2, y1 + height), fill=fill, outline=outline)
    drawer.rectangle((x1, y2 - radius, x1 + width, y2), fill=fill, outline=outline)
    drawer.rectangle((x1 + radius, y2, x2 - radius, y2), fill=fill, outline=outline)
    drawer.rectangle((x1, y1, x2 - radius, y1), fill=fill, outline=outline)
    drawer.rectangle((x1 + radius, y1, x2, y2), fill=fill, outline=outline)

    # Save the image with the rounded rectangle
    image.save(output_path)

# Parameters for the image with a rounded rectangle
image_path = 'input_image.png'   # Path of the input image
output_path = 'output_image.png'  # Path to save the output image
width = 200
height = 100
radius = 10
outline = 'black'
fill = 'white'

# Call the function to draw the rounded rectangle
draw_rounded_rectangle(image_path, output_path, width, height, radius, outline, fill)
