from PIL import Image, ImageDraw, ImageFont

# Create a bitmap for the text.

img = Image.new('RGB', (100, 50), color='white')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial.ttf', 16)
draw.text((10, 10), "Hello, World!", font=font, fill='black')
img.show()