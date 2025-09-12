from PIL import Image

def get_bounding_box(image_path):
    # Load the image
    img = Image.open(image_path)

    # Convert the image to grayscale
    img_gray = img.convert('L')

    # Apply threshold to convert the image to binary
    img_binary = img_gray.point(lambda p: p > 0 and 255, '1')

    # Convert the binary image to a matrix
    img_matrix = list(img_binary.getdata())
    img_matrix = [img_matrix[i:i+img_binary.width] for i in range(0, len(img_matrix), img_binary.width)]

    # Calculate the bounding box
    bbox = (len(img_matrix[0]), len(img_matrix), 0, 0)
    for y in range(len(img_matrix)):
        for x in range(len(img_matrix[0])):
            if img_matrix[y][x] != 0:
                if x < bbox[0]:
                    bbox = (x, bbox[1], bbox[2], bbox[3])
                if x > bbox[2]:
                    bbox = (bbox[0], bbox[1], x, bbox[3])
                if y < bbox[1]:
                    bbox = (bbox[0], y, bbox[2], bbox[3])
                if y > bbox[3]:
                    bbox = (bbox[0], bbox[1], bbox[2], y)

    return bbox

# Replace "image_path" with the actual path to your image
bounding_box = get_bounding_box("image_path")

print(f"The bounding box of the non-zero regions is: {bounding_box}")
