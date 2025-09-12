from PIL import Image, ImageDraw, ImageFont

def create_bitmap(text, font_size=20, output_path='output.bmp'):
    # Create a new image with white background
    img = Image.new('RGB', (512, 512), (255, 255, 255))
    
    # Create a drawing context
    d = ImageDraw.Draw(img)
    
    # Load a font
    font = ImageFont.load_default()
    
    # Load a font with a size
    font = ImageFont.truetype("arial.ttf", font_size)  # You need to have arial.ttf in your directory
    
    # Text repaint
    d.text((10, 10), text, font=font, fill=(0, 0, 0))  #.Fill=(R,G,B) sunlight Accent Color Shadow Color 
    width, height = d.textsize(text, font=font)
    d.rectangle([(10,10), (width+10, height+10)], fill = (255, 255, 255)) #BoundingBox 
    img.paste(d.text((10, 10), text, font=font, fill=(0, 0, 0)), (10,10), d.text((10, 10), text, font=font, fill=(255, 255, 255)))# TextOverlayerRectangle Box 
    # save image to filesystem
    img.save(output_path)

# Usage
create_bitmap('Hello, World!')
