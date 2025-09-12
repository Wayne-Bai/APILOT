from PIL import Image, ImageDraw
import numpy as np

def round_corner(radius, fill):
    """Draw a round corner"""
    corner = Image.new('RGBA', (radius, radius), (0, 0, 0, 0))
    draw = ImageDraw.Draw(corner)
    draw.pieslice((0, 0, radius * 2, radius * 2), 180, 270, fill=fill)
    return corner

def rounded_rectangle(size, radius, fill, border=None):
    """Draw a rounded rectangle"""
    width, height = size
    rectangle = Image.new('RGBA', size, fill)
    corner = round_corner(radius, fill)

    # Draw rectangular parts
    rectangle.paste(corner, (0, 0))
    rectangle.paste(corner.rotate(90), (0, height - radius))
    rectangle.paste(corner.rotate(180), (width - radius, height - radius))
    rectangle.paste(corner.rotate(270), (width - radius, 0))

    # Draw straight lines
    draw = ImageDraw.Draw(rectangle)
    draw.rectangle([(radius, 0), (width - radius, height)], fill=fill)
    draw.rectangle([(0, radius), (width, height - radius)], fill=fill)

    # Add border
    if border:
        draw.rounded_rectangle([(0, 0), (width-1, height-1)], radius=radius, outline=border)

    return rectangle
