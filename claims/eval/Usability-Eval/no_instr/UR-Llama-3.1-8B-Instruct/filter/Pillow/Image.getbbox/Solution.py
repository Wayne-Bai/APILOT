from PIL import Image

# Load the image
img = Image.open('image.bmp')  # replace 'image.bmp' with your image file

# Convert the image to grayscale
img_gray = img.convert('L')

# Get the non-zero pixels (background noise)
non_zero_pixels = img_gray.load()
non_zero_pixels_list = [(x, y) for x in range(img_gray.size[0]) for y in range(img_gray.size[1]) if non_zero_pixels[x, y]!= 0]

# Get the minimum and maximum coordinates of the non-zero pixels
min_x, min_y = min(non_zero_pixels_list, key=lambda pt: (pt[1], pt[0]))
max_x, max_y = max(non_zero_pixels_list, key=lambda pt: (pt[1], pt[0]))

# Print the bounding box coordinates
print("Minimum x:", min_x)
print("Minimum y:", min_y)
print("Maximum x:", max_x)
print("Maximum y:", max_y)

# Print the bounding box area
area = (max_x - min_x) * (max_y - min_y)
print("Bounding box area:", area)
