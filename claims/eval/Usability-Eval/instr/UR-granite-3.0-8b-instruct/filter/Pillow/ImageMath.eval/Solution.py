from PIL import Image, ImageMath

def evaluate_image_expression(image_path, expression):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to float
    img = img.convert('RGB')
    img = img.split()
    r, g, b = img
    r = r.point(lambda i: i / 1.0)
    g = g.point(lambda i: i / 1.0)
    b = b.point(lambda i: i / 1.0)
    img = ImageMath.eval(expression, {'r': r, 'g': g, 'b': b})
    img = img.point(lambda i: i * 255)
    img = ImageMath.eval('r*0.299 + g*0.587 + b*0.114', {'r': img, 'g': img, 'b': img})
    img = img.convert('L')

    return img
