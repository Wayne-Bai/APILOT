from PIL import Image

# Store 2D vector data
data = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Convert 2D list to image
image = Image.new("L", (3, 3), 1)
for i in range(len(data)):
    for j in range(len(data[i])):
        image.putpixel((j, i), data[i][j])

# Save the image
image.save("vector_data_image.png")
