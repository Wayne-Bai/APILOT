from PIL import Image

def calculate_bounding_box(image_path):
    # Open the image using Pillow
    img = Image.open(image_path)

    # Convert the image to RGB if it's not already
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Convert the image data to a list of lists
    data = list(img.getdata())

    # Create a list of the bounding box coordinates
    bbox = [0, 0, 0, 0]

    # Iterate over the pixels in the image
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            # If the pixel is not zero
            if sum(data[i + j * img.size[0]]) != 0:
                # Update the bounding box coordinates
                bbox[0] = min(bbox[0], i)
                bbox[1] = min(bbox[1], j)
                bbox[2] = max(bbox[2], i)
                bbox[3] = max(bbox[3], j)

    return bbox
