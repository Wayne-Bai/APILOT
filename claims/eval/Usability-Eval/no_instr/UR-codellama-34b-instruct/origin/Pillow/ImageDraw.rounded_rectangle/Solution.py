
from PIL import Image, ImageDraw

def draw_rounded_rectangle(image, xy, radius):
    draw = ImageDraw.Draw(image)
    (x1, y1), (x2, y2) = xy
    draw.pieslice((x1, y1, x2, y2), 0, 90, fill=None, outline=(0, 0, 0))
    draw.pieslice((x2 - radius, y1, x2, y1 + radius), 90, 180, fill=None, outline=(0, 0, 0))
    draw.pieslice((x1, y2 - radius, x1 + radius, y2), 180, 270, fill=None, outline=(0, 0, 0))
    draw.pieslice((x1, y1, x1 + radius, y1 + radius), 270, 360, fill=None, outline=(0, 0, 0))

# Example usage:
image = Image.new('RGB', (500, 300), (255, 255, 255))
draw_rounded_rectangle(image, ((100, 50), (400, 250)), 20)
image.show()
