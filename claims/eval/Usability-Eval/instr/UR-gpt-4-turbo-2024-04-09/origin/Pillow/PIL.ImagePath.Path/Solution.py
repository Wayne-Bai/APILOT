from PIL import Image

# Load an existing image
input_image_path = 'path_to_your_image.jpg'
output_image_path = 'path_to_save_resized_image.jpg'
img = Image.open(input_image_path)

# Define new dimensions (width, height) as a 2D vector
new_dimensions = (800, 600)  # Resize dimensions in pixels

# Resize the image
resized_img = img.resize(new_dimensions)

# Save the resized image
resized_img.save(output_image_path)

print(f"Image resized to dimensions: {new_dimensions} and saved to {output_image_path}")
