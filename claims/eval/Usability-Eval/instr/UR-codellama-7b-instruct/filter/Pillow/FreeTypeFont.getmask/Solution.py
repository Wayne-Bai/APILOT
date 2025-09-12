
import PIL.Image, PIL.ImageDraw, PIL.ImageFont

# Create an image with the given size
image = PIL.Image.new("RGB", (500, 300), (255, 255, 255))

# Create a font object using the FreeSans font and set its size to 48 pixels
font = PIL.ImageFont.truetype("FreeSans.ttf", 48)

# Draw the text on the image at (10, 10) with the specified color and thickness
draw = PIL.ImageDraw.Draw(image)
draw.text((10, 10), "Hello, world!", font=font, fill=(0, 0, 0))

# Save the image to a file
image.save("hello_world.bmp")
