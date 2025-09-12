
from PIL import Image, ImageDraw, ImageFont

text = "Hello, World!"
font_size = 30
font = ImageFont.truetype("arial.ttf", font_size)

width, height = font.getsize(text)
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)
draw.text((0, 0), text, font=font, fill="black")

image.show()
