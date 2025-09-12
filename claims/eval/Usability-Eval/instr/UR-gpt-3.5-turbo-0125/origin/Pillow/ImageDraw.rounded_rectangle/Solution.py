
from PIL import Image, ImageDraw

def draw_rounded_rectangle(draw, xy, rad, fill=None, outline=None):
    x0, y0, x1, y1 = xy
    r = rad

    draw.rectangle([x0+r, y0, x1-r, y1], fill=fill, outline=outline)
    draw.rectangle([x0, y0+r, x0+r, y1-r], fill=fill, outline=outline)
    draw.rectangle([x1-r, y0+r, x1, y1-r], fill=fill, outline=outline)

    draw.pieslice([x0, y0, x0 + r*2, y0 + r*2], 180, 270, fill=fill, outline=outline)
    draw.pieslice([x1 - r*2, y0, x1, y0 + r*2], 270, 360, fill=fill, outline=outline)
    draw.pieslice([x0, y1 - r*2, x0 + r*2, y1], 90, 180, fill=fill, outline=outline)
    draw.pieslice([x1 - r*2, y1 - r*2, x1, y1], 0, 90, fill=fill, outline=outline)

img = Image.new('RGB', (400, 400), color='white')
draw = ImageDraw.Draw(img)
draw_rounded_rectangle(draw, (50, 50, 350, 350), 30, fill='blue', outline='black')

img.show()
