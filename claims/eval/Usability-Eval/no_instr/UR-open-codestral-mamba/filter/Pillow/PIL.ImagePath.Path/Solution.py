from PIL import Image
import numpy as np

# Create a new blank image with white background
def create_image(size: tuple = (640, 480)):
    return Image.new("RGB", size, "white")

# Create a new image with a checkerboard pattern
def create_checkerboard_image(size: tuple = (640, 480)):
    image = create_image(size)
    pixels = np.array(image)

    for i in range(0, size[1], 20):
        for j in range(0, size[0], 20):
            if (i // 20 + j // 20) % 2 == 0:
                pixels[i:i+20, j:j+20] = [0, 0, 0]  # black
            else:
                pixels[i:i+20, j:j+20] = [255, 255, 255]  # white

    return Image.fromarray(pixels, 'RGB')

checkerboard_image = create_checkerboard_image()
checkerboard_image.show()
