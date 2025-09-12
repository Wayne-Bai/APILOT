from PIL import Image, ImageDraw, ImageFont

width, height = 500, 500
background_color = (0, 0, 0)

# create a black background
image = Image.new('RGB', (width, height), background_color)
draw = ImageDraw.Draw(image)

# specify a message and font
message = "Hello, World!"
font_size = 25
font = ImageFont.truetype('arial.ttf', font_size)

# calculate text size
text_width, text_height = draw.textsize(message, font)

# calculate text position
text_position = ((width - text_width) / 2, (height - text_height) / 2)

# actual text input to the image
draw.text(text_position, message, fill=(255, 255, 255), font=font)

# save the image
image.save('output_image.png')
