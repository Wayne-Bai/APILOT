
from PIL import Image, ImageDraw

def draw_rounded_rectangle(draw, xy, corner_radius, fill=None, outline=None):
    upper_left = xy[0], xy[1] + corner_radius
    upper_right = xy[0] + corner_radius, xy[1]
    lower_right = xy[2] - corner_radius, xy[3]
    lower_left = xy[2], xy[3] - corner_radius

    draw.arc((upper_left, (xy[0] + corner_radius * 2, xy[1] + corner_radius * 2)), 180, 270, fill=fill, outline=outline)
    draw.arc((upper_right, (xy[0] + corner_radius * 2, xy[1] + corner_radius * 2)), 270, 360, fill=fill, outline=outline)
    draw.arc((lower_right, (xy[0] + corner_radius * 2, xy[1] + corner_radius * 2)), 0, 90, fill=fill, outline=outline)
    draw.arc((lower_left, (xy[0] + corner_radius * 2, xy[1] + corner_radius * 2)), 90, 180, fill=fill, outline=outline)

    draw.line((xy[0] + corner_radius, xy[1]), (xy[2] - corner_radius, xy[1]), fill=fill, width=1)
    draw.line((xy[2], xy[1] + corner_radius), (xy[2], xy[3] - corner_radius), fill=fill, width=1)
    draw.line((xy[2] - corner_radius, xy[3]), (xy[0] + corner_radius, xy[3]), fill=fill, width=1)
    draw.line((xy[0], xy[3] - corner_radius), (xy[0], xy[1] + corner_radius), fill=fill, width=1)

image = Image.new("RGB", (400, 400), (255, 255, 255))
draw = ImageDraw.Draw(image)
draw_rounded_rectangle(draw, (50, 50, 350, 350), corner_radius=50, fill=(255, 0, 0), outline=(0, 0, 0))

image.show()
