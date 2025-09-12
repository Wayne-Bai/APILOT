from PIL import Image

# create a new image with a white background
image = Image.new("RGB", (500, 500), "white")

# create a drawing object
draw = ImageDraw.Draw(image)

# choose a font
font = ImageFont.truetype("arial.ttf", 50)

# draw the text
draw.text((100, 100), "Hello, world!", font=font)

# save the image
image.save("hello.png")
