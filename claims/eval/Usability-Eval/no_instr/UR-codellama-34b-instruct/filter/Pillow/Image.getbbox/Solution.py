from PIL import Image, ImageDraw

# Load the image
image = Image.open("image_file.jpg")

# Get the width and height of the image
width, height = image.size

# Create a new image with the same size as the original
new_image = Image.new("RGB", (width, height))

# Loop through each pixel in the image
for x in range(width):
    for y in range(height):
        # Get the current pixel value
        pixel = image.getpixel((x, y))
        
        # Check if the pixel is not 0
        if pixel != 0:
            # Calculate the bounding box of the non-zero region
            x1, y1, x2, y2 = new_image.getbbox()
            
            # Draw a rectangle around the non-zero region
            draw = ImageDraw.Draw(new_image)
            draw.rectangle((x1, y1, x2, y2), fill=None, outline="red")
            
            # Save the new image
            new_image.save("output_file.jpg", quality=95)
