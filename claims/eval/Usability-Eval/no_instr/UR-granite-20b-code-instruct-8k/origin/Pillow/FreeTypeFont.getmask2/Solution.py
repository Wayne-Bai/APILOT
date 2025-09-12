
from PIL import Image, ImageDraw, ImageFont

# create a blank image
img = Image.new("RGB", (200, 100), color="white")

# get a drawing context
draw = ImageDraw.Draw(img)

# load a font
font = ImageFont.truetype("arial.ttf", 36)

# draw text
draw.text((10, 10), "Hello, World!", font=font)

# save the image
img.save("hello.png")
