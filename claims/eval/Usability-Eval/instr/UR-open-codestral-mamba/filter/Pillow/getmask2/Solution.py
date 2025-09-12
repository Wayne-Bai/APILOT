from PIL import Image, ImageDraw, ImageFont

def create_bitmap_for_text(text, font_path, save_path):
    # create image
    img = Image.new('RGB', (1000, 300), color = (73, 109, 137))

    # create draw object
    d = ImageDraw.Draw(img)

    # set font type and size
    fnt = ImageFont.truetype(font_path, 40)

    # add text to image
    d.text((10, 10), text, font=fnt, fill=(255, 255, 0))

    # show or save image
    img.save(save_path)

# use in command line with valid file paths
if __name__ == "__main__":
    create_bitmap_for_text("Hello, World!", "/path/to/your/font.ttf", "/path/to/your/output.jpg")
