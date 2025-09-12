from PIL import Image, ImageDraw

def draw_rounded_rectangle(draw, xy, radius, **kwargs):
    x0, y0, x1, y1 = xy
    draw.rectangle((x0+radius, y0, x1-radius, y1), **kwargs)
    draw.rectangle((x0, y0+radius, x0+radius, y1-radius), **kwargs)
    draw.rectangle((x1-radius, y0+radius, x1, y1-radius), **kwargs)
    draw.ellipse((x0, y0, x0+2*radius, y0+2*radius), **kwargs)
    draw.ellipse((x1-2*radius, y0, x1, y0+2*radius), **kwargs)
    draw.ellipse((x0, y1-2*radius, x0+2*radius, y1), **kwargs)
    draw.ellipse((x1-2*radius, y1-2*radius, x1, y1), **kwargs)

def main():
    # Initialize the image
    width, height = 400, 200
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    # Draw a rectangle with rounded corners
    xy = (50, 50, 350, 150)  # Top-left and bottom-right coordinates
    radius = 20  # Corner radius
    fill_color = (135, 206, 235)  # Light sky blue
    outline_color = (0, 0, 0)  # Black

    draw_rounded_rectangle(draw, xy, radius, fill=fill_color, outline=outline_color)

    # Save the image
    img.save('rounded_rectangle.png')

if __name__ == "__main__":
    main()
