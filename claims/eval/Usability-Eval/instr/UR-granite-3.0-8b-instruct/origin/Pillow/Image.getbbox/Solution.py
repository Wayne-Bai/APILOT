from PIL import Image, ImageMath

def calculate_bounding_box(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Convert the image to grayscale
    img_gray = img.convert('L')

    # Calculate the bounding box of the non-zero regions
    # This is done by creating a mask of the non-zero regions and then finding the bounding box of the mask
    mask = img_gray.point(lambda x: x > 0 and 255)
    mask_bbox = mask.getbbox()

    # Return the bounding box as a tuple of (x, y, width, height)
    return mask_bbox
